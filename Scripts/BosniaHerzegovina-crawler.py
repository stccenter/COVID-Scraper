'''
@Author: your name
@Date: 2020-05-31 22:37:39
@LastEditTime: 2020-06-14 15:15:50
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
'''
import requests
import urllib.request
import urllib.parse
from urllib import request
from bs4 import BeautifulSoup
import os
import time
from datetime import datetime

begin_time = datetime.now()

url = 'http://mcp.gov.ba/publication/read/sluzbene-informacije-o-koronavirusu-covid-19'
# strhtml = requests.get(url)
# soup = BeautifulSoup(strhtml.text,'lxml')
# img = soup.select('#top > div.main-content > section.rte.w-max > accordions:nth-child(14) > div.accordion.card.accordion-open > div > div > p:nth-child(21) > img')
# urllib.request.urlretrieve(img,'D:/google drive/crawler/%s.jpg"%(x)')

response = requests.get(url, headers={'Connection': 'close'})
soup = BeautifulSoup(response.content, 'lxml')
items = soup.find_all('img')

mkfile_time = datetime.strftime(datetime.now(), '%Y%m%d%H%M')

folder_path = './data/Bosnia&Herzegovina/'+ mkfile_time + '/'
if os.path.exists(folder_path) == False:  # 判断文件夹是否已经存在
    os.makedirs(folder_path)

for image in items:
    print(image.get('src'))

items.pop(0)
items.pop(2)
items.pop(1)

basewebsite = 'http://mcp.gov.ba'

for image in items:
		html = image.get('src')
		htmlnew = urllib.parse.urljoin(basewebsite,html)


#try:
for index, item in enumerate(items):
	if item:
		# get函数获取图片链接地址，requests发送访问请求
		#html = requests.get(item.get('src'))
		html = item.get('src')
		htmlnew = urllib.parse.urljoin(basewebsite,html)
		html = requests.get(htmlnew)
		img_name = folder_path + str(index + 1) + '.png'
		with open(img_name, 'wb') as file:  # 以byte形式将图片数据写入
			file.write(html.content)
			file.flush()
		file.close()  # 关闭文件
		print('第%d张图片下载完成' % (index+1))
		time.sleep(1)
		 # 自定义延时
print('抓取完成')

print(datetime.now() - begin_time)
