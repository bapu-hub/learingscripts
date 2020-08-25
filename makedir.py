#!/usr/bin/env python
# -*- coding: utf-8 -*-
def mkdir(path):
    # 引入模块
    import os
    path=path.strip()
    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists=os.path.exists(path)
    for i in range(int(folder_nums)):
        
    # 判断结果
        if not isExists:
            folder_name=path+"test_%num"%i
           
            os.makedirs(folder_name) 
     
            print path+' 创建成功'
            #return True
        else:
            # 如果目录存在则不创建，并提示目录已存在
            print path+' 目录已存在'
            #return False
     
# 定义要创建的目录

mkpath=raw_input("请输入要创建文件夹的目录： ")
folder_nums=raw_input("请输入要创建文件夹的数量： ")
# 调用函数

