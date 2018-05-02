#!usr/bin/env python  
#-*- coding:utf-8 _*-  
""" 
   @author:xd 
   @file: process_image_rotate.py 
   @time: 2018/04/28
"""

import os
from PIL import Image

dir_name = os.path.dirname(__file__)
file_path = os.path.join(dir_name,'player_all_image')

files = os.listdir(file_path)

print(len(files))
print(files)

# idx = 0
for file in files:
    tmp_file_path = os.path.join(file_path,file)
    player_images = os.listdir(tmp_file_path)
    if 'hot_map.png' == player_images[0]:
        # idx += 1
        player_hot_map = os.path.join(tmp_file_path,player_images[0])
        img = Image.open(player_hot_map)
        img = img.rotate(180)
        img.save(player_hot_map)

# print(idx)