'''
@Author: Matthew Shabet
@Date: 2020-09-14 19:51:00
@LastEditTime: 2020-11-12 23:48:00
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
'''
import csv
import requests
import os
from datetime import datetime
from bs4 import BeautifulSoup
import time

begin_time = datetime.now()
regions = ["Eastern Cape", "Free State", "Gauteng", "KwaZulu-Natal", "Limpopo", "Mpumalanga", "North West", "Northern Cape", "Western Cape"]

url = "https://sacoronavirus.co.za/category/press-releases-and-notices/"

# Get the data url
response = requests.get(url, headers={'Connection': 'close'})
soup = BeautifulSoup(response.content, 'html.parser')
tag = soup.findAll("div", {"class": "fusion-posts-container fusion-blog-layout-grid fusion-blog-layout-grid-4 isotope fusion-blog-equal-heights fusion-blog-pagination fusion-blog-rollover"})
pages = tag[0].contents[1::2]

links = [p.contents[1].contents[3].contents[1].contents[1].contents[0]["href"] for p in pages]
link = [l for l in links if l.find("update-on-covid-19") >= 0][0]
# Get the data
response = requests.get(link, headers={'Connection': 'close'})
soup = BeautifulSoup(response.content, 'html.parser')
tags = soup.findAll("img")

mkfile_time = datetime.strftime(datetime.now(), '%Y%m%d%H%M')
print(mkfile_time)

folder_path = './data/SouthAfrica/'+ mkfile_time + '/'
if os.path.exists(folder_path) == False:  # 判断文件夹是否已经存在
    os.makedirs(folder_path)

index = 1
for item in tags:
    html = requests.get(item.get('src'))
    img_name = folder_path + str(index) + '.png'
    print(img_name)
    with open(img_name, 'wb') as file:
        file.write(html.content)
        file.flush()
    file.close()
    print('第%d张图片下载完成' % (index))
    index += 1
    time.sleep(1)  # 自定义延时

print(datetime.now() - begin_time)