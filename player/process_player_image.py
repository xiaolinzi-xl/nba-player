#!usr/bin/env python  
#-*- coding:utf-8 _*-  
""" 
   @author:xd 
   @file: process_player_image.py 
   @time: 2018/04/20
"""

import os
from PIL import Image
import json

dir_name = 'download_avatar'

dir_path = os.path.join(os.path.dirname(__file__),dir_name)

files = os.listdir(dir_path)

# print(dir_path)
# print(files)

dir_new_name = os.path.join(os.path.dirname(__file__),'player_all_image')

# file = files[0]
error_ids = []
for file in files:
    file_name = os.path.join(dir_path,file)

    dir_tmp = os.path.join(dir_new_name,file[:-4])

    if not os.path.exists(dir_tmp):
        os.makedirs(dir_tmp)
    file_new_name = os.path.join(dir_tmp,'pic.png')

    try:
        tmp = Image.open(file_name)
        tmp.save(file_new_name)
    except Exception as e:
        print(e)
        error_ids.append(file[:-4])

error_file = os.path.join(os.path.dirname(__file__),'error_id.json')
with open(error_file,'w') as f:
    f.write(json.dumps(error_ids))
