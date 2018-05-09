# -*- coding:utf-8 -*-
""" 
   @author: xiaolinzi
   @file: requests_download_player_base.py 
   @time: 2018/05/09
"""
import requests
import json
import os

dir_name = os.path.dirname(__file__)
file_name = os.path.join(dir_name,'team_all.json')

with open(file_name,'r') as f:
    data = json.load(f)

base_url = 'https://stats.nba.com/stats/commonteamroster?LeagueID=00&Season=2017-18&TeamID=%s'
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}

player_datas = []

for team in data:
    url = base_url % team['id']
    response = requests.get(url,headers=header)
    content = response.json()
    # print(content)
    # print(type(content))
    for player in content['resultSets'][0]['rowSet']:
        team_id = team['id']
        player_id = player[-1]
        name = player[3]
        cloth_num = player[4]
        pos = player[5]
        height = player[6]
        weight = player[7]
        # print(name)

        player_data = {}
        player_data['team_id'] = team_id
        player_data['player_id'] = player_id
        player_data['name'] = name
        player_data['cloth_num'] = cloth_num
        player_data['pos'] = pos
        player_data['height'] = height
        player_data['weight'] = weight

        player_datas.append(player_data)


file_name = os.path.join(dir_name,'new_player_base_1.json')
with open(file_name,'w') as f:
    f.write(json.dumps(player_datas))

print(len(player_datas))

