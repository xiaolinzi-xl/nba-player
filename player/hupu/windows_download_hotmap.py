# -*- coding:utf-8 -*-
""" 
   @author: xiaolinzi
   @file: windows_download_hotmap.py 
   @time: 2018/05/10
"""

from selenium import webdriver
from scrapy.selector import Selector
import base64
import json
import time
import os

options = webdriver.ChromeOptions()
options.set_headless()
chrome_path = 'F:/tmp/chromedriver.exe'
browser = webdriver.Chrome(executable_path=chrome_path,chrome_options=options)


js = '''function getimage() {
    var myCanvas = document.getElementById("myCanvas");
    var image = myCanvas.toDataURL("image/png").replace("data:image/png;base64,", "");
    var spanTag = document.createElement("span");
    spanTag.id = "canvasimage";
    spanTag.innerHTML =image;
    spanTag.style.display = "none";
    document.body.appendChild(spanTag);
}

    getimage();

'''

dir_name = os.path.dirname(__file__)
file_name = os.path.join(dir_name, 'hupu_player_3.json')

with open(file_name, 'r') as f:
    data = json.load(f)

base_url = 'https://games.mobileapi.hupu.com/1/7.1.18/nba/playerPage?client=861945035683907&player_id={player_id}&night=0&entrance=1'

for player in data:
    name = player['name']
    player_id = player['player_id']
    url = base_url.format(player_id=player_id)

    browser.get(url)
    time.sleep(5)
    browser.execute_script(js)
    html = Selector(text=browser.page_source)

    map_img = html.css('#canvasimage::text').extract_first()
    # print(base64)

    image_data = base64.b64decode(map_img)

    dir_path = os.path.join(dir_name, 'hotmap_image')
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    file_name = os.path.join(dir_path, name + '.png')
    file = open(file_name, 'wb')
    file.write(image_data)
    file.close()
# browser.find_element_by_css_selector('ul.tab.clearfix li.tab-map').click()

browser.close()