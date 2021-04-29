'''
@Author: Yifei Tian
@Date: 2020-06-07 21:58:10
@LastEditTime: 2020-06-07 22:28:29
@LastEditors: Please set LastEditors
@Description: In User Settings Edit

'''
import requests
import os
import time
from datetime import datetime

url = ' https://services5.arcgis.com/rlT6XQbCNBKBXh0u/arcgis/rest/services/cazuricovid19moldovaoperational18_viewfor_test/FeatureServer/0/query?where=1%3D1&outFields=*&f=json'

mkfile_time = datetime.strftime(datetime.now(), '%Y%m%d%H%M')
#print(mkfile_time)

folder_path = './data/Moldova/'+ mkfile_time + '/'
if os.path.exists(folder_path) == False:  # 判断文件夹是否已经存在
    os.makedirs(folder_path)

try:
    r = requests.get(url)
    with open(folder_path + "data.json", "wb") as code:
        code.write(r.content)
        print('抓取完成')
except IOError:
 	print("error")