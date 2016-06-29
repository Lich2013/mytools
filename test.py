#! /usr/bin/env python
# coding: utf8
import os

# def getFilesSize(path):
dir = '/Users/Lich/www'
size = 0
for root, dirs, files in os.walk(dir):
	size += sum([os.path.getsize(join(root, name)) for name in files])
	print size
	# print root, dirs, files