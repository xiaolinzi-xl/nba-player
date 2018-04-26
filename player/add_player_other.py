#!usr/bin/env python  
#-*- coding:utf-8 _*-  
""" 
   @author:xd 
   @file: add_player_other.py 
   @time: 2018/04/24
"""

# 增加球员
import requests
from scrapy.selector import Selector
import json
import os

dir_name = os.path.dirname(__file__)
file_name= os.path.join(dir_name,'player_base.json')

with open(file_name,'r') as f:
    data = json.load(f)

base_url = 'http://stats.nba.com/player/%s/'

player_datas = []

header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}

for player in data:
    url = base_url % player['player_id']
    response = requests.get(url=url,headers=header)
    html = Selector(text=response.text)

    country = html.css('div.player-stats__prior span::text').re_first('.*?/(.*)')
    draft = html.css('div.player-stats__draft span::text').extract_first()
    birthday = html.css('div.player-stats__birthdate span::text').extract_first()

    player_data = dict(player)

    player_data['country'] = country
    player_data['birthday'] = birthday
    player_data['draft'] = draft

    player_datas.append(player_data)

file_name = os.path.join(dir_name,'player_all.json')
with open(file_name,'w') as f:
    f.write(json.dumps(player_datas))

print(len(player_datas))

