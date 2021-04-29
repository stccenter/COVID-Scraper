'''
@Author: Matthew Shabet
@Date: 2020-08-30 18:00:00
@LastEditTime: 2020-08-30 18:20:00
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
'''
import csv
import requests
import os
from datetime import datetime

url = "https://www.stopcovid19.jp/data/covid19japan.csv"

with requests.Session() as s:
	download = s.get(url)
	decode = download.content.decode('utf-8')
	cr = csv.reader(decode.splitlines(), delimiter=',')
	data = list(cr)

	# Create and open the CSV
	mkfile_time = datetime.strftime(datetime.now(), '%Y%m%d%H%M')
	folder_path = './data/Japan/'+ mkfile_time + '/'
	if not os.path.exists(folder_path):
	    os.makedirs(folder_path)
	file = open(folder_path+'table.csv', 'w', newline='', encoding='utf-8-sig')
	writer = csv.writer(file)

	# Write each row to the csv
	for row in data:
		writer.writerow(row)