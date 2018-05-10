# -*- coding:utf-8 -*-
""" 
   @author: xiaolinzi
   @file: requests_download_season_base.py 
   @time: 2018/05/09
"""
# 有问题，会报错
# http.client.RemoteDisconnected: Remote end closed connection without response

import requests
import json
import os
import time

dir_name = os.path.dirname(__file__)
file_name = os.path.join(dir_name, 'player_all.json')

with open(file_name, 'r') as f:
    data = json.load(f)

base_url = 'https://stats.nba.com/stats/playerdashboardbyyearoveryear?DateFrom=&DateTo=&GameSegment=&LastNGames=0&LeagueID=00&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=PerGame&Period=0&PlayerID=%s&PlusMinus=N&Rank=N&Season=2017-18&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&Split=yoy&VsConference=&VsDivision='
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}

season_datas = []

for player in data:
    url = base_url % player['player_id']
    response = requests.get(url, headers=header)
    time.sleep(1)
    content = response.json()

    season_data = {}
    season_data['player_id'] = player['player_id']
    season_data['team_id'] = player['team_id']
    season_data['season_type'] = content['parameters']['SeasonType']
    season_data['season_data'] = content['resultSets'][1]['rowSet']

    season_datas.append(season_data)

file_name = os.path.join(dir_name, 'new_season_base_1.json')

with open(file_name, 'w') as f:
    f.write(json.dumps(season_datas))

print(len(season_datas))
