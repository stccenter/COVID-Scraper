'''
@Author: Yifei Tian
@Date: 2020-06-07 21:58:10
@LastEditTime: 2020-06-07 22:11:32
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \crawler\Jamaica-crawler.py
'''
import requests
import os
import time
from datetime import datetime

url = 'https://admin.jamcovid19.moh.gov.jm/public/api/statistics'

mkfile_time = datetime.strftime(datetime.now(), '%Y%m%d%H%M')
#print(mkfile_time)

folder_path = './data/Jamaica/'+ mkfile_time + '/'
if os.path.exists(folder_path) == False:  # 判断文件夹是否已经存在
    os.makedirs(folder_path)

try:
    r = requests.get(url)
    with open(folder_path + "data.json", "wb") as code:
        code.write(r.content)
        print('抓取完成')
except IOError:
 	print("error")