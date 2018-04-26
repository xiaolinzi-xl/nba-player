#!usr/bin/env python  
#-*- coding:utf-8 _*-  
""" 
   @author:xd 
   @file: download_team_1.py 
   @time: 2018/04/24
"""

from selenium import webdriver
import os

browser = webdriver.Chrome()

url = "https://stats.nba.com/teams/"

browser.get(url)

page = browser.page_source

browser.close()

dir_name = os.path.dirname(__file__)
file_name = os.path.join(dir_name,'team.html')

with open(file_name,'w') as f:
    f.write(page)

