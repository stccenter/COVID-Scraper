'''
@Author: Yifei Tian
@Date: 2020-06-07 21:58:10
@LastEditTime: 2020-06-26 14:03:24
@LastEditors: Please set LastEditors
@Description: In User Settings Edit

'''
import requests
import os
import time
import pandas as pd 
from datetime import datetime

url = 'https://services3.arcgis.com/CoIPqtHxRZqBsYyb/arcgis/rest/services/FORM2_1/FeatureServer/0/query?where=1%3D1&returnGeometry=false&outFields=*&f=json'

mkfile_time = datetime.strftime(datetime.now(), '%Y%m%d%H%M')


folder_path = './data/Libya/'+ mkfile_time + '/'
if os.path.exists(folder_path) == False:  # 判断文件夹是否已经存在
    os.makedirs(folder_path)

try:
    r = requests.get(url)
    with open(folder_path + "data.json", "wb") as code:
        code.write(r.content)
        print('抓取完成')
except IOError:
 	print("error")

# df = pd.read_json(url)
# print (df)