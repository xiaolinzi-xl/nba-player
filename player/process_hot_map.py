#!usr/bin/env python  
#-*- coding:utf-8 _*-  
""" 
   @author:xd 
   @file: process_hot_map.py 
   @time: 2018/04/20
"""

import json
import os
from PIL import Image

dir_name = os.path.dirname(__file__)
file_name = os.path.join(dir_name,'player_filter.json')

with open(file_name,'r') as f:
    data = json.load(f)

# print(data)

name_dict = {}

for player in data:
    name_dict[player['name']] = player['player_id']

print(len(name_dict))


hupu_dir = os.path.join(os.path.dirname(__file__),'hupu','hotmap_image')

dir_insert = os.path.join(os.path.dirname(__file__),'player_all_image')

files = os.listdir(hupu_dir)
# idx = 0
error_map = []
for file in files:
    player_name = file[:-4]
    if player_name in name_dict:
        player_id = str(name_dict[player_name])

        dir_tmp = os.path.join(dir_insert,player_id)
        if not os.path.exists(dir_tmp):
            os.makedirs(dir_tmp)
        file_path = os.path.join(dir_tmp,'hot_map.png')

        old_file_path = os.path.join(hupu_dir,file)
        try:
            tmp = Image.open(old_file_path)
            tmp.save(file_path)
        except Exception as e:
            print(e)
            error_map.append(player_id)
# print(files)
# print(idx)

error_path = os.path.join(os.path.dirname(__file__),'error_hotmap_2.json')

with open(error_path,'w') as f:
    f.write(json.dumps(error_map))