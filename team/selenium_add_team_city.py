# -*- coding:utf-8 -*-
""" 
   @author: xiaolinzi
   @file: selenium_add_team_city.py 
   @time: 2018/05/09
"""
from selenium import webdriver
from scrapy.selector import Selector
import os
import json


dir_name = os.path.dirname(__file__)
file_name = os.path.join(dir_name,'new_team_1.json')

with open(file_name,'r') as f:
    data = json.load(f)

base_url = 'https://stats.nba.com/stats/teamdetails?teamID={}'

chrome_path = 'F:/tmp/chromedriver.exe'
# options = webdriver.ChromeOptions()
# options.set_headless()
# 注意，不要用无界面爬取数据，中途可能会报错
browser = webdriver.Chrome(executable_path=chrome_path)

team_datas = []

for team in data:
    url = base_url.format(team['id'])
    browser.get(url)
    html = Selector(text=browser.page_source)
    team_data = html.css("pre::text").extract_first()
    team_data = json.loads(team_data)
    city = team_data['resultSets'][0]['rowSet'][0][4]

    res = dict(team)
    res['city'] = city
    team_datas.append(res)


file_name = os.path.join(dir_name,'new_team_all.json')
with open(file_name, 'w') as f:
    f.write(json.dumps(team_datas))

browser.close()
