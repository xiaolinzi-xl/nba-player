#!usr/bin/env python  
#-*- coding:utf-8 _*-  
""" 
   @author:xd 
   @file: download_season_base.py 
   @time: 2018/04/24
"""

# 获取球员赛季基本数据
# 使用Selenium 爬取json数据，10min左右
# 使用Scrapy 爬取json数据，20min左右

from selenium import webdriver
import json
from scrapy.selector import Selector
import os

dir_name = os.path.dirname(__file__)
file_name = os.path.join(dir_name,'player_all.json')

with open(file_name,'r') as f:
    data = json.load(f)

chrome_path = 'F:/tmp/chromedriver.exe'
browser = webdriver.Chrome(executable_path=chrome_path)

base_url = 'https://stats.nba.com/stats/playerdashboardbyyearoveryear?DateFrom=&DateTo=&GameSegment=&LastNGames=0&LeagueID=00&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=PerGame&Period=0&PlayerID=%s&PlusMinus=N&Rank=N&Season=2017-18&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&Split=yoy&VsConference=&VsDivision='

season_datas = []

for player in data:
    url = base_url % player['player_id']
    browser.get(url)
    html = Selector(text=browser.page_source)
    page = html.css('pre::text').extract_first()
    content = json.loads(page)

    season_data = {}
    season_data['player_id'] = player['player_id']
    season_data['team_id'] = player['team_id']
    season_data['season_type'] = content['parameters']['SeasonType']
    season_data['season_data'] = content['resultSets'][1]['rowSet']

    season_datas.append(season_data)

browser.close()

file_name = os.path.join(dir_name,'season_base_5.json')

with open(file_name,'w') as f:
    f.write(json.dumps(season_datas))

print(len(season_datas)) # 505
