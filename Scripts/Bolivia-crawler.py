'''
@Author: Yifei Tian
@Date: 2020-05-31 22:37:39
@LastEditTime: 2020-06-24 18:02:05
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
'''
import requests
from urllib import request
from bs4 import BeautifulSoup
import os
import time
from datetime import datetime
import pandas as pd
begin_time = datetime.now()
url = 'https://www.boliviasegura.gob.bo/'


response = requests.get(url, headers={'Connection': 'close'})
soup = BeautifulSoup(response.content, 'lxml')
items = soup.find_all("div", {"class": "carousel-item"})
mkfile_time = datetime.strftime(datetime.now(), '%Y%m%d%H%M')

folder_path = './data/Bolivia/' + mkfile_time + '/'

if os.path.exists(folder_path) == False:  # 判断文件夹是否已经存在
    os.makedirs(folder_path)

for index, item in enumerate(items):
    image = item.img['src']
    html = requests.get(image)
    img_name = folder_path + str(index + 1) + '.png'
    with open(img_name, 'wb') as file:
        file.write(html.content)
        file.flush()
    file.close()
    print('第%d张图片下载完成' % (index+1))
    time.sleep(1)  # 自定义延时
