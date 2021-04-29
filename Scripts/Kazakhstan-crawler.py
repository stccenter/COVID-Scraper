'''
@Author: Leon Tian
@Date: 2020-05-31 22:37:39
@LastEditTime: 2020-06-06 18:10:02
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

url = 'https://www.coronavirus2020.kz/'


response = requests.get(url, headers={'Connection': 'close'})
soup = BeautifulSoup(response.content, 'lxml')
case = soup.select('.last_info_covid_bl')[0].text
recovery = soup.select('.red_line_covid_bl')[0].text
death = soup.select('.deaths_bl')[0].text

mkfile_time = datetime.strftime(datetime.now(), '%Y%m%d%H%M')


folder_path = './data/Kazakhstan/'+ mkfile_time + '/'
if os.path.exists(folder_path) == False:  # 判断文件夹是否已经存在
     os.makedirs(folder_path)

try:
     f = open(folder_path + 'case.txt', 'wb')
     f.write(str(case).encode('utf-8-sig'))
     f.close()

     f = open(folder_path + 'recovery.txt', 'wb')
     f.write(str(recovery).encode('utf-8-sig'))
     f.close()

     f = open(folder_path + 'death.txt', 'wb')
     f.write(str(death).encode('utf-8-sig'))
     f.close()

except IOError:
 	print("error")

