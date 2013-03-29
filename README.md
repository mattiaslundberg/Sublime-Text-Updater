Sublime-Text-Updater
====================

Simple updater for sublime text 2 and 3 in python. Intended for use with .tar.bz2 versions for Linux.

Requires Python 2 and [PyQuery](https://pypi.python.org/pypi/pyquery) installed.

Edit update_subl.py and set the required version of sublime text (Default 2 - 32bit) at the top of the file. If installation in /opt/ is not wanted change this to desired path.
To update/install sublime text at the specified version run "sudo python update_subl.py".

Optionally creates symbolic link in /usr/bin.
