#!usr/bin/env python  
#-*- coding:utf-8 _*-  
""" 
   @author:xd 
   @file: download_team_info.py 
   @time: 2018/04/24
"""

from scrapy.selector import Selector
import json
import os

dir_name = os.path.dirname(__file__)
file_name = os.path.join(dir_name,'team.html')

with open(file_name,'r') as f:
    html = f.read()

page = Selector(text=html)

team_datas = []

for team in page.css('div.stats-team-list div.landing__leaders-body section.landing__leaders-category table.category-table tbody tr td.category-table__text'):
    id = team.css('a::attr(href)').re_first('/team/(\d+)/')
    name = team.css('a::text').extract()[-1].strip()

    team_data = {}
    team_data['id'] = id
    team_data['name'] = name

    team_datas.append(team_data)

file_name = os.path.join(dir_name,'team_1.json')

with open(file_name,'w') as f:
    f.write(json.dumps(team_datas))

print(len(team_datas))