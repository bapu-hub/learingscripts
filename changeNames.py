# -*- coding: utf-8 -*-
"""
Created on Sat Jan 04 09:00:59 2020
change the names of folders and files under specify path
@author: bli5
"""
import os, sys
def get_input():
    while True:
        filepath=input('请输入文件夹地址：')
        old = input('请输入需要被更换的字符串：')
        new = input('请输入新字符串：')
        if len(filepath)>0  and len(old)>0:
            return [filepath,old,new]
        else:print('请重新输入')

def change_str(data):
    filepath=data[0]
    old=data[1]
    new=data[2]
    os.chdir(filepath)
    for root, dirs, files in os.walk('.'):
      for name in files: #change file names
          pathName=os.path.join(root,name)
          newName=name.replace(old,new)
          newPathName=os.path.join(root,newName)
          if name!=newName: 
              print (name,newName)
              os.rename(pathName,newPathName)
      for dir in dirs:#change dirs names
          pathdir = os.path.join(root, dir)
          newdir=dir.replace(old,new)
          newpathdir=os.path.join(root, newdir)
          if pathdir!=newpathdir:
              os.rename(pathdir,newpathdir)         
if __name__=='__main__':
    data =get_input()
    change_str(data)
   

