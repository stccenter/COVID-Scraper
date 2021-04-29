'''
Author: your name
Date: 2020-06-01 17:23:44
LastEditTime: 2021-01-28 21:20:46
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \crawler\Hungary-crawler.py
'''
import requests
from urllib import request
from bs4 import BeautifulSoup
import os
import time
from datetime import datetime

begin_time = datetime.now()
url = 'https://koronavirus.gov.hu/'

response = requests.get(url, headers={'Connection': 'close'})
soup = BeautifulSoup(response.content, 'lxml')
items = soup.find_all('img')

mkfile_time = datetime.strftime(datetime.now(), '%Y%m%d%H%M')


folder_path = './data/Hungary/'+ mkfile_time + '/'
if os.path.exists(folder_path) == False:
    os.makedirs(folder_path)


items.pop(0)
items.pop(0)
items.pop(0)
items.pop(0)
items.pop(0)


	
try:
	for index, item in enumerate(items):
		if item:
			html = requests.get(item.get('src'))
			print(html)
			img_name = folder_path + str(index + 1) + '.png'
			with open(img_name, 'wb') as file:  
				file.write(html.content)
				file.flush()
			file.close() 
			print('%dth pictures saved!' % (index+1))
			time.sleep(1) 
	print('done!')

except IOError:
	print("error")
	
print(datetime.now() - begin_time)