#!/usr/bin/python
"""
Copyright (c) 2013, Mattias Lundberg
All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

  * Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
  * Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

import urllib, subprocess, os, re, sys

is_py3 = sys.version_info[0] == 3
if is_py3:
	import urllib.request as urllib
else:
	def input(*args):
		return raw_input(*args)

version = '2' # Valid choices are '2', '3' and '3dev'
arch = 32

url = 'http://www.sublimetext.com/%s' % version
subl_folder = '/tmp/'

def _get_latest_urls():
	sock = urllib.urlopen(url)
	data = sock.read().decode('utf-8') if is_py3 else sock.read()
	return re.search("linux[ ,\w,_,-]+%s.*href\=\"(.*?\.tar\.bz2)\""  % arch, data)

def main():
	download = _get_latest_urls().group(1)
	
	assert download != None, 'Download URL not found!'
	
	print( 'Updating to %s' % download )
	
	filename = download.split('/')[-1]
	
	sock = urllib.urlopen(download)
	data = sock.read()
	rawfile = open(subl_folder + filename, 'wb')
	rawfile.write(data)
	rawfile.close()
	
	print( 'Extracting "tar xf %s"' % (subl_folder + filename) )
	subprocess.Popen(['tar', 'xf', filename], cwd = subl_folder)
	
	syml = input("Create symlink in /usr/bin for 'sublime_text' (y/[n]): ")
	
	if 'y' in syml:
		print( 'Creating symlink' )
		if '3' in version:
			subprocess.Popen(['ln', '-s', '%ssublime_text_3/sublime_text' % (subl_folder)], cwd = '/usr/bin')
		else:
			subprocess.Popen(['ln', '-s', '%sSublime Text 2/sublime_text' % (subl_folder)], cwd = '/usr/bin')
	
	print( 'Done installing Sublime Text' )

if __name__ == '__main__':
	main()
