# -*- coding:utf-8 -*-
""" 
   @author: xiaolinzi
   @file: windows_process_image_rotate.py 
   @time: 2018/05/10
"""

import os
from PIL import Image

dir_name = os.path.dirname(__file__)
file_path = os.path.join(dir_name,'hotmap_image')

new_file_path = os.path.join(dir_name,'rotate_hotmap_image')
if not os.path.exists(new_file_path):
    os.makedirs(new_file_path)

files = os.listdir(file_path)

print(len(files))
# print(files)

# idx = 0
for file in files:
    player_hot_map = os.path.join(file_path,file)
    new_image_path = os.path.join(new_file_path,file)
    # print(player_hot_map)
    img = Image.open(player_hot_map)
    img = img.rotate(180)
    img.save(new_image_path)


# print(idx)