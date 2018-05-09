# -*- coding:utf-8 -*-
""" 
   @author: xiaolinzi
   @file: selenium_download_team_info.py 
   @time: 2018/05/09
"""

from selenium import webdriver
from scrapy.selector import Selector
import os
import json

chrome_path = 'F:/tmp/chromedriver.exe'
browser = webdriver.Chrome(executable_path=chrome_path)

url = 'https://stats.nba.com/teams/'

browser.get(url)

page = Selector(text=browser.page_source)

browser.close()

team_datas = []

for team in page.css('div.stats-team-list div.landing__leaders-body section.landing__leaders-category table.category-table tbody tr td.category-table__text'):
    id = team.css('a::attr(href)').re_first('/team/(\d+)/')
    name = team.css('a::text').extract()[-1].strip()

    team_data = {}
    team_data['id'] = id
    team_data['name'] = name

    team_datas.append(team_data)

dir_name = os.path.dirname(__file__)
file_name = os.path.join(dir_name,'new_team_1.json')

with open(file_name,'w') as f:
    f.write(json.dumps(team_datas))

print(len(team_datas))
