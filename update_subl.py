#!/usr/bin/python
import urllib, subprocess, os, re
from pyquery import PyQuery as pq

url = 'http://www.sublimetext.com/2'
subl_folder = '/opt/'

def _get_latest_url():
	dom = pq(url=url)
	
	return dom('#dl_linux_64 > a')[0].get('href')

def _cmp_version(old, new):
	def normalize(v):
		return [int(x) for x in re.sub(r'(\.0+)*$','', v).split(".")]
	return cmp(normalize(old), normalize(new))

def main():
	latest_url = _get_latest_url()
	
	version = latest_url.split(' ')[2]
	filename = latest_url.split('/')[-1]
	
	try:
		old_version_file = file('%slatest_version' % subl_folder, 'r')
		old_version = old_version_file.readline().replace('\n','').replace('^M','')
		old_version_file.close()
	except IOError:
		old_version = '0'
	
	if _cmp_version(old_version, version) >= 0:
		print 'No updates found'
		return
	else:
		print 'Updating from %s to %s' % (old_version, version)
		old_version_file = file('%slatest_version' % subl_folder, 'w')
		old_version_file.write(version)
		old_version_file.close
	
	mysock = urllib.urlopen(latest_url)
	rawdata = mysock.read()
	rawfile = file(subl_folder + filename, 'wb')
	rawfile.write(rawdata)
	rawfile.close()
	
	out = subprocess.check_output(['ls', subl_folder])
	
	if 'Sublime Text 2' in out.split('\n'):
		print 'Backing up old version'
		subprocess.Popen(['mv', '%sSublime Text 2' % subl_folder, '%sSublime Text %s backup' % (subl_folder, old_version)])
	
	subprocess.Popen(['tar', 'xf', subl_folder + filename])
	
	print 'Done!'

if __name__ == '__main__':
	main()