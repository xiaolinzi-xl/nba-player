# -*- coding: utf-8 -*-

import json
import os

def get_data(file_name):
    dirname = os.path.dirname(__file__)
    file_path = os.path.join(dirname,file_name)

    try:
        file = open(file_path,'r')
        data = json.load(file)
        file.close()
        return data
    except Exception as e:
        print(e)


def get_common(nba_data,hupu_data):
    hupu_dict = {}
    for idx in range(len(hupu_data)):
        hupu_dict[hupu_data[idx]['name']] = idx

    common_datas = []
    for player in nba_data:
        if player['name'] in hupu_dict:
            common_data = dict(player)
            team_id = int(common_data['team_id'])
            common_data['team_id'] = team_id

            tmp_birthday = player['birthday'].split('/')
            common_data['birthday'] = tmp_birthday[2] + '-' + tmp_birthday[0] + '-' + tmp_birthday[1]

            tmp_hei = player['height'].split('-')
            height = (int(tmp_hei[0]) * 12 + int(tmp_hei[1])) * 2.54
            common_data['height'] = int(height) / 100  # 单位是米

            tmp_wei = player['weight']
            weight = int(tmp_wei) * 0.4535924
            common_data['weight'] = int(weight)  # 单位是千克

            idx = hupu_dict[player['name']]
            hupu_player = hupu_data[idx]
            common_data['salary'] = int(hupu_player['salary'])

            common_data['armspan'] = 0.0
            common_data['reach_height'] = 0.0
            if 'armspan' in hupu_player:
                common_data['armspan'] = float(hupu_player['armspan'])
            if 'reach_height' in hupu_player:
                common_data['reach_height'] = float(hupu_player['reach_height'])

            common_datas.append(common_data)


    return common_datas


def save_data(data,file_name):
    try:
        dirname = os.path.dirname(__file__)
        file_path = os.path.join(dirname,file_name)
        file = open(file_path,'w')
        file.write(json.dumps(data))
        file.close()
        return True
    except Exception as e:
        print(e)

if __name__ == '__main__':
    hupu_data = get_data('hupu/hupu_player_4.json')
    nba_data = get_data('player_all.json')

    print(len(hupu_data)) # 489
    print(len(nba_data)) # 505
    data = get_common(nba_data=nba_data,hupu_data=hupu_data)
    print(len(data)) # 490 486
    # print(data)
    print(save_data(data,'player_filter.json'))
