#!usr/bin/env python  
#-*- coding:utf-8 _*-  
""" 
   @author:xd 
   @file: download_player_base.py 
   @time: 2018/04/24
"""

# 获取球员基本信息 player_id,team_id,name,cloth_num,pos,height,weight


from selenium import webdriver
from scrapy.selector import Selector
import json
import os

dir_name = os.path.dirname(__file__)
file_name = os.path.join(dir_name,'team_all.json')

with open(file_name,'r') as f:
    data = json.load(f)

browser = webdriver.Chrome()

base_url = 'https://stats.nba.com/stats/commonteamroster?LeagueID=00&Season=2017-18&TeamID=%s'
player_datas = []

for team in data:
    url = base_url % team['id']
    browser.get(url)
    html = Selector(text=browser.page_source)
    page = html.css('pre::text').extract_first()
    content = json.loads(page)
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

browser.close()

file_name = os.path.join(dir_name,'player_base.json')
with open(file_name,'w') as f:
    f.write(json.dumps(player_datas))

print(len(player_datas))
