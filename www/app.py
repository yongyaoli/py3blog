#! /usr/bin/env python3
#-*- coding: utf-8 -*-

#/Users/liyongyao/work/python/blog_env/bin/python3.6.exe
import sys
import os


print(sys.version)
print(sys.version_info)

print(os.path.abspath(__file__)) # 绝对路径， 加文件名
print(os.path.split(os.path.realpath(__file__))[0])
print('info...')