# -*- coding: utf-8 -*-
"""
Created on Sat Jan 04 09:00:59 2020
change the names of directories and files
@author: bli5
"""
import os, sys
os.chdir(r"F:\learn\python\test\change names")
for root, dirs, files in os.walk('.'):
  for name in files: #change file names
      pathName=os.path.join(root,name)
      newName=name.replace('Rivian','Rivian-2')
      newPathName=os.path.join(root,newName)
      if name!=newName: 
          print (name,newName)
          os.rename(pathName,newPathName)
  for dir in dirs:#change dirs names
      pathdir = os.path.join(root, dir)
      newdir=dir.replace('Rivian','Rivian-2')
      newpathdir=os.path.join(root, newdir)
      if pathdir!=newpathdir:
          os.rename(pathdir,newpathdir)         
print 'change done'

