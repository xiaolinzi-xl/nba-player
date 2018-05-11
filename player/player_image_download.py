#!usr/bin/env python  
#-*- coding:utf-8 _*-  
""" 
   @author:xd 
   @file: player_image_download.py 
   @time: 2018/04/20
"""

import json
import requests
import os
from multiprocessing import Pool
import time

def get_data(file_name):
    directory = os.path.dirname(__file__)
    file_path = os.path.join(directory,file_name)

    try:
        with open(file_path,'r') as f:
            data = json.load(f)
            return data
    except Exception as e:
        print(e)

def get_download_req(data):
    base_url = 'https://ak-static.cms.nba.com/wp-content/uploads/headshots/nba/{team_id}/2017/260x190/{player_id}.png'

    req_list = []
    for player in data:
        team_id = str(player['team_id'])
        player_id = str(player['player_id'])

        url = base_url.format(team_id=team_id,player_id=player_id)
        # dirname = os.path.join(os.path.dirname(__file__),'player_image',player_id)
        dirname = os.path.join(os.path.dirname(__file__),'player_avatar_2')
        file_path = os.path.join(dirname,'{}.png'.format(player_id))

        req_list.append((url,dirname,file_path))
    return req_list

def make_directory(dirname):
    if not os.path.exists(dirname):
        try:
            os.makedirs(dirname)
        except Exception as e:
            print(e)
    return True

def download_image(req):
    url,dirname,file_path = req
    if os.path.exists(file_path):
        print('exists')
        return
    try:
        response = requests.get(url)
        make_directory(dirname)

        with open(file_path,'wb') as f:
            f.write(response.content)

    except Exception as e:
        print(e)


def multi_process_image(req_list,processes=4):
    start_time = time.time()

    # pool = Pool(processes=processes)

    for req in req_list:
        # 201577,203898,201935
        # pool.apply_async(download_image,(req,))
        download_image(req)

    # pool.close()
    # pool.join()
    end_time = time.time()
    print('下载完毕,用时:%s秒' % (end_time - start_time))

if __name__ == '__main__':
    file_name = 'player_filter.json'
    data = get_data(file_name)
    req_list = get_download_req(data)

    multi_process_image(req_list)