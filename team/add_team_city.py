#!usr/bin/env python  
#-*- coding:utf-8 _*-  
""" 
   @author:xd 
   @file: add_team_city.py 
   @time: 2018/04/24
"""

from selenium import webdriver
import json
import os
from scrapy.selector import Selector

dir_name = os.path.dirname(__file__)
file_name = os.path.join(dir_name,'team_1.json')

with open(file_name,'r') as f:
    data = json.load(f)

base_url = 'https://stats.nba.com/stats/teamdetails?teamID=%s'

browser = webdriver.Chrome()

team_datas = []

for team in data:
    url = base_url % team['id']
    browser.get(url)
    html = Selector(text=browser.page_source)
    team_data = html.css("pre::text").extract_first()
    team_data = json.loads(team_data)
    city = team_data['resultSets'][0]['rowSet'][0][4]

    res = dict(team)
    res['city'] = city
    team_datas.append(res)


file_name = os.path.join(dir_name,'team_all.json')
with open(file_name, 'w') as f:
    f.write(json.dumps(team_datas))

browser.close()
