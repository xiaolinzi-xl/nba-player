#!usr/bin/env python  
#-*- coding:utf-8 _*-  
""" 
   @author:xd 
   @file: download_season_advanced.py 
   @time: 2018/04/24
"""

from selenium import webdriver
from scrapy.selector import Selector
import json
import os

dir_name = os.path.dirname(__file__)
file_name = os.path.join(dir_name,'player_all.json')

with open(file_name,'r') as f:
    data = json.load(f)

browser = webdriver.Chrome()

base_url = 'https://stats.nba.com/stats/playerdashboardbyyearoveryear?DateFrom=&DateTo=&GameSegment=&LastNGames=0&LeagueID=00&Location=&MeasureType=Advanced&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=PerGame&Period=0&PlayerID=%s&PlusMinus=N&Rank=N&Season=2017-18&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&Split=yoy&VsConference=&VsDivision='

season_datas = []
error_urls = []

for player in data:
    player_id = player['player_id']
    team_id = player['team_id']

    url = base_url % player_id
    browser.get(url)
    source_code = browser.page_source
    html = Selector(text=source_code)
    page = html.css('pre::text').extract_first()
    # if page is None or len(page) == 0:
    #     continue
    try:
        content = json.loads(page)
        row_datas = content['resultSets'][1]['rowSet']
        for row_data in row_datas:
            # if int(row_data[2]) == int(team_id):
            season_data = {}
            season_data['player_id'] = player_id
            season_data['team_id'] = team_id
            season_data['team_name'] = row_data[3]
            season_data['season'] = row_data[1]
            season_data['type'] = 'Regular Season'
            season_data['efg_pct'] = row_data[20]
            season_data['ts_pct'] = row_data[21]
            season_data['ortg'] = row_data[10]
            season_data['drtg'] = row_data[11]

            season_datas.append(season_data)
    except Exception as e:
        print(e)
        error_url = {}
        error_url['player_id'] = player_id
        error_url['url'] = url
        error_urls.append(error_url)

browser.close()


file_name = os.path.join(dir_name,'season_base_3.json')
with open(file_name, 'w') as f:
    f.write(json.dumps(season_datas))

file_name = os.path.join(dir_name,'error.json')
with open(file_name,'w') as f:
    f.write(json.dumps(error_urls))

print(error_urls)
