#!usr/bin/env python  
#-*- coding:utf-8 _*-  
""" 
   @author:xd 
   @file: download_player_info.py 
   @time: 2018/04/24
"""

import requests
import os
from scrapy.selector import Selector
import json
import re

'''
HTTPSConnectionPool(host='nba.hupu.com', port=443): Max retries exceeded with url:

总结：自己写的会抛异常,使用 scrapy 框架爬取,不会抛异常. 有3个球员抛异常了 490 + 3
'''

def get_team_url(url):
    team_urls = []
    try:
        response = requests.get(url)
        page = Selector(text=response.text)
        for team_url in page.css('div.team a::attr(href)').extract():
            if team_url:
                team_urls.append(team_url)
    except Exception as e:
        print(e)
    return team_urls

def get_player_url(team_urls):
    player_urls = []
    try:
        for team_url in team_urls:
            response = requests.get(team_url)
            page = Selector(text=response.text)
            for player_url in page.css('div.x_list a::attr(href)').extract():
                if player_url:
                    player_urls.append(player_url)
    except Exception as e:
        print(e)
    return player_urls

def get_player_info(player_urls):
    player_infos = []
    for player_url in player_urls:
        try:
            response = requests.get(player_url)
            page = Selector(text=response.text)
            name = page.css('title::text').extract_first().split('|')[1]
            player_id = re.findall('.*?(\d+).html', response.url)[0]
            raw_salary = page.css('div.font p::text').extract()[-2]
            salary = re.findall('.*?(\d+).*', raw_salary)[0]

            player_info = {}
            player_info['name'] = name.strip()
            player_info['player_id'] = player_id
            player_info['salary'] = salary
            player_info['url'] = response.url

            player_infos.append(player_info)

        except Exception as e:
            print(e)
            print(player_url)

    return player_infos


def save_data(file_name,data):
    dir_name = os.path.dirname(__file__)
    file_path = os.path.join(dir_name,file_name)
    try:
        with open(file_path,'w') as f:
            f.write(json.dumps(data))
    except Exception as e:
        print(e)


if __name__ == '__main__':
    url = 'https://nba.hupu.com/teams'
    team_urls = get_team_url(url)
    print(len(team_urls))

    player_urls = get_player_url(team_urls)
    print(len(player_urls))
    player_infos = get_player_info(player_urls)
    print(len(player_infos))
    save_data('hupu_player_1.json',player_infos)