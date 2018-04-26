#!usr/bin/env python  
#-*- coding:utf-8 _*-  
""" 
   @author:xd 
   @file: request_json_test.py 
   @time: 2018/04/24
"""

# 测试 requests 抓取 json 包

import json
from scrapy.selector import Selector
import requests


base_url = 'https://stats.nba.com/stats/commonteamroster?LeagueID=00&Season=2017-18&TeamID={team_id}'
url = base_url.format(team_id='1610612751')

header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}

try:
    response = requests.get(url=url,headers=header,timeout=10)
    # print(response.json())
    print(response.text)
except Exception as e:
    print(e)

