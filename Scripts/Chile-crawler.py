'''
@Author: Yifei Tian
@Date: 2020-05-31 22:37:39
@LastEditTime: 2020-07-21 18:40:59
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

url = 'https://www.minsal.cl/nuevo-coronavirus-2019-ncov/casos-confirmados-en-chile-covid-19/'


response = requests.get(url, headers={'Connection': 'close'})
soup = BeautifulSoup(response.content, 'lxml')
tables = soup.select('table')



mkfile_time = datetime.strftime(datetime.now(), '%Y%m%d%H%M')

folder_path = './data/Chile/'+ mkfile_time + '/'
if os.path.exists(folder_path) == False:  # 判断文件夹是否已经存在
    os.makedirs(folder_path)

table_name = folder_path +'.csv'

    
try:
    df = pd.read_html(tables[0].prettify())
    #print(df)
    df = pd.concat(df)
    df.to_csv(folder_path+'table.csv', encoding='utf-8-sig')
    print('Crawler has been completed successfully!')
except IOError:
 	print("error")
