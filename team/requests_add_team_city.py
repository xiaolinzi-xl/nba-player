# -*- coding:utf-8 -*-
""" 
   @author: xiaolinzi
   @file: requests_add_team_city.py 
   @time: 2018/05/09
"""
import requests
import json
import os

dir_name = os.path.dirname(__file__)
file_name = os.path.join(dir_name,'new_team_1.json')

with open(file_name,'r') as f:
    data = json.load(f)

base_url = 'https://stats.nba.com/stats/teamdetails?teamID={}'
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}

team_datas = []

for team in data:
    url = base_url.format(team['id'])
    response = requests.get(url,headers=header)
    team_data = response.json()
    city = team_data['resultSets'][0]['rowSet'][0][4]

    res = dict(team)
    res['city'] = city
    team_datas.append(res)


file_name = os.path.join(dir_name,'new_team_all_1.json')
with open(file_name, 'w') as f:
    f.write(json.dumps(team_datas))

