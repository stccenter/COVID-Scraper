'''
@Author: Yifei Tian
@Date: 2020-05-31 22:37:39
@LastEditTime: 2020-06-24 17:57:06
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
url = 'https://www.sozialministerium.at/Informationen-zum-Coronavirus/Neuartiges-Coronavirus-(2019-nCov).html'


response = requests.get(url, headers={'Connection': 'close'})
soup = BeautifulSoup(response.content, 'lxml')
tables = soup.select('table')


mkfile_time = datetime.strftime(datetime.now(), '%Y%m%d%H%M')

folder_path = './data/Austria/'+ mkfile_time + '/'
if os.path.exists(folder_path) == False:  # 判断文件夹是否已经存在
    os.makedirs(folder_path)

table_name = folder_path +'.csv'

convert_dict = {'Bgld.': int, 
                'Ktn.': int,
                'NÖ': int, 
                'OÖ': int, 
                'Sbg.': int, 
                'Stmk.': int, 
                'T': int, 
                'W': int, 
                'Vbg.': int, 
                'Austria as a whole': int, 
               } 
try:
    df = pd.read_html(tables[0].prettify())
    df = pd.concat(df)
    df = df.rename(columns={"Bundesland":"states", "Österreich  gesamt":"Austria as a whole"})
    #pd.to_numeric(pd,downcast='signed')
    df = df.rename(index={0:"Confirmed cases", 1:"Deaths", 2:"Recover", 3:"Hospitalization ", 4:"Intensive care unit", 5:"Tests "})
    #df = df.astype(convert_dict) 
    df.to_csv(folder_path+'table.csv', encoding='utf-8-sig')
    print('抓取完成')
except IOError:
 	print("error")

print(datetime.now() - begin_time)
