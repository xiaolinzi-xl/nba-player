#!usr/bin/env python  
#-*- coding:utf-8 _*-  
""" 
   @author:xd 
   @file: process_season_db.py 
   @time: 2018/04/24
"""

import os
import json

dir_name = os.path.dirname(__file__)
file_name = os.path.join(dir_name,'season_base_2.json')

with open(file_name,'r') as f:
    data1 = json.load(f)

file_name = os.path.join(dir_name,'season_base_3.json')

with open(file_name,'r') as f:
    data2 = json.load(f)

print(len(data1))
print(len(data2))

season_datas = []

for season1, season2 in zip(data1, data2):
    # key = str(season['player_id']) + season['season']
    season_data = dict(season1)
    # if key in season_dict:
    #     tmp = season_dict[key]
    if season1['player_id'] != season2['player_id'] or season1['season'] != season2['season']:
        print(season1['player_id'])
        continue
    season_data['efg_pct'] = season2['efg_pct']
    season_data['ts_pct'] = season2['ts_pct']
    season_data['ortg'] = season2['ortg']
    season_data['drtg'] = season2['drtg']
    season_datas.append(season_data)

file_name = os.path.join(dir_name,'season_base_4.json')
with open(file_name, 'w') as f:
    f.write(json.dumps(season_datas))
