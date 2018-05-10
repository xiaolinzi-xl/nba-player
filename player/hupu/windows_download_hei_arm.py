# -*- coding:utf-8 -*-
""" 
   @author: xiaolinzi
   @file: windows_download_hei_arm.py 
   @time: 2018/05/10
"""

from selenium import webdriver
import json
from scrapy.selector import Selector
import os


dir_name = os.path.dirname(__file__)
file_name = os.path.join(dir_name,'hupu_player_3.json')

with open(file_name,'r') as f:
    data = json.load(f)

options = webdriver.ChromeOptions()
options.set_headless()
chrome_path = 'F:/tmp/chromedriver.exe'
browser = webdriver.Chrome(executable_path=chrome_path,chrome_options=options)

base_url = 'https://games.mobileapi.hupu.com/1/7.1.18/nba/playerPage?client=861945035683907&player_id={player_id}&night=0&entrance=1'

insert_players = []

for player in data:

    name = player['name']
    player_id = player['player_id']
    salary = player['salary']

    url = base_url.format(player_id=player_id)

    # browser.execute_async_script(js)
    browser.get(url)

    page = Selector(text=browser.page_source)
    # print(html)

    insert_player = {}
    insert_player['name'] = name
    insert_player['salary'] = salary
    body = page.css('ul.section.body-list div.num span::text').extract()
    if len(body) == 8:
        armspan = body[2].strip()
        reach_height = body[4].strip()
        insert_player['armspan'] = armspan
        insert_player['reach_height'] = reach_height

    insert_players.append(insert_player)

    # print(body)
    # print(armspan)
    # print(reach_height)

browser.close()

print(len(insert_players))
file_name = os.path.join(dir_name,'hupu_player_4.json')

with open(file_name,'w') as f:
    f.write(json.dumps(insert_players))
