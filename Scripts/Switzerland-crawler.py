'''
@Author: Yifei Tian
@Date: 2020-06-07 21:58:10
@LastEditTime: 2020-06-08 13:54:57
@LastEditors: Please set LastEditors
@Description: In User Settings Edit

'''
import requests
import os
import time
from datetime import datetime

url = 'https://www.bag.admin.ch/dam/bag/de/dokumente/mt/k-und-i/aktuelle-ausbrueche-pandemien/2019-nCoV/covid-19-datengrundlage-lagebericht.xlsx.download.xlsx/200325_Datengrundlage_Grafiken_COVID-19-Bericht.xlsx'

mkfile_time = datetime.strftime(datetime.now(), '%Y%m%d%H%M')
#print(mkfile_time)

folder_path = './data/Switzerland/'+ mkfile_time + '/'
if os.path.exists(folder_path) == False:  # 判断文件夹是否已经存在
    os.makedirs(folder_path)

try:
    r = requests.get(url)
    with open(folder_path + "data.xlsx", "wb") as code:
        code.write(r.content)
        print('抓取完成')
except IOError:
 	print("error")