#!usr/bin/env python  
#-*- coding:utf-8 _*-  
""" 
   @author:xd 
   @file: process_season_base.py 
   @time: 2018/04/24
"""

import json
import os

dir_name = os.path.dirname(__file__)
file_name = os.path.join(dir_name,'season_base_1.json')

with open(file_name,'r') as f:
    data = json.load(f)

season_datas = []

for player in data:
    player_id = player['player_id']
    team_id = player['team_id']
    tmp_datas = player['season_data']
    type = player['season_type']
    # print(team_id)

    for tmp_data in tmp_datas:
        # print(type(season_data[2]))
        # print(type(team_id))
        season = tmp_data[1]
        team_name = tmp_data[3]
        gp = tmp_data[5]
        min = tmp_data[9]
        reb = tmp_data[21]
        fg_pct = tmp_data[12]
        fg3_pct = tmp_data[15]
        ft_pct = tmp_data[18]

        pts = tmp_data[29]
        ast = tmp_data[22]
        oreb = tmp_data[19]
        dreb = tmp_data[20]
        stl = tmp_data[24]
        blk = tmp_data[25]
        tov = tmp_data[23]
        fgm = tmp_data[10]
        fga = tmp_data[11]
        fg3m = tmp_data[13]

        season_type = type
        # print(season,pts,ast,oreb,dreb,stl,blk,tov,fgm,fga,fg3m)
        # print(season_data)

        season_data = {}
        season_data['player_id'] = player_id
        season_data['team_id'] = team_id
        season_data['season'] = season
        season_data['type'] = season_type
        season_data['team_name'] = team_name

        season_data['gp'] = gp
        season_data['min'] = min
        season_data['reb'] = reb
        season_data['fg_pct'] = fg_pct
        season_data['fg3_pct'] = fg3_pct
        season_data['ft_pct'] = ft_pct

        season_data['pts'] = pts
        season_data['ast'] = ast
        season_data['oreb'] = oreb
        season_data['dreb'] = dreb
        season_data['stl'] = stl
        season_data['blk'] = blk
        season_data['tov'] = tov
        season_data['fgm'] = fgm
        season_data['fga'] = fga
        season_data['fg3m'] = fg3m

        season_datas.append(season_data)

file_name = os.path.join(dir_name,'season_base_2.json')
with open(file_name,'w') as f:
    f.write(json.dumps(season_datas))

print(len(season_datas))
