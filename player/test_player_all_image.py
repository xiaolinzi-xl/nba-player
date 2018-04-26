#!usr/bin/env python  
#-*- coding:utf-8 _*-  
""" 
   @author:xd 
   @file: test_player_all_image.py 
   @time: 2018/04/26
"""

import os

dir_name = os.path.dirname(__file__)
dir_path = os.path.join(dir_name,'player_all_image')

files = os.listdir(dir_path)

print(len(files))

print(files[:4])
print(files[-1:-4:-1])
print(files[-1])