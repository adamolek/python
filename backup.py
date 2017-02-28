#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import shutil

def copy_recursive(src, dest):
	for file_name in os.listdir(src):
		src_file = os.path.join(src, file_name)
		dest_file = os.path.join(dest, file_name)
		if os.path.isdir(src_file) == True:
			if os.path.exists(dest_file) == False:
				os.makedirs(dest_file)
			copy_recursive(src_file, dest_file)
		else:
			src_time = os.path.getmtime(src_file)
			try:
				dest_time = os.path.getmtime(dest_file)
			except OSError:
				dest_time = 0
			
                        if round(src_time) > round(dest_time):
				print "Current copied file:", src_file
				shutil.copy2(src_file, dest_file)
			else:
				print "File", src_file, "is already backed-up"

if len(sys.argv) != 3:
	print "Usage:"
	print "\t./backup.py source_directory backup_directory"
	exit()
#end if

src_dir = sys.argv[1]
backup_dir = sys.argv[2]

if os.path.exists(src_dir) == False:
	print "source_directory doesn't exist!!!"
	exit()


if os.path.exists(backup_dir) == False:
	os.makedirs(backup_dir)

copy_recursive(src_dir, backup_dir)

print "Done"
