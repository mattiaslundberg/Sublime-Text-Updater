Sublime-Text-Updater
====================

Simple updater for Sublime Text 2 and 3 in Python. Intended for use with .tar.bz2 versions for Linux.

Usage: python update_subl.py [-h] [-a ARCH] [-v VERSION] [-f SUBL_FOLDER] [-s]

Update the Sublime Text editor.

```
Command line arguments:
-h, --help - show help message and exit
-a ARCH, --architecture ARCH - Architecture ([32]/64).
-v VERSION, --version VERSION - Version to download ([2]/3/3dev).
-f SUBL_FOLDER, --folder SUBL_FOLDER - Location for installation of Sublime Text [/opt/].
-s, --symlink - Enable creation of symlink in /usr/bin for 'sublime_text'.
```
