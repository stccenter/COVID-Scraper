'''
@Author: Matthew Shabet
@Date: 2020-10-03 21:51:00
@LastEditTime: 2020-10-03 22:48:00
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
'''
import csv
import requests
import json
import os
from datetime import datetime

url = 'https://www.fhi.no/api/chartdata/api/91322'

# Get the data
response = requests.get(url, headers={'Connection': 'close'})
data = json.loads(response.text)[1:]

# Create and open the CSV
mkfile_time = datetime.strftime(datetime.now(), '%Y%m%d%H%M')
folder_path = './data/Norway/'+ mkfile_time + '/'
if not os.path.exists(folder_path):
    os.makedirs(folder_path)
file = open(folder_path+'table.csv', 'w', newline='', encoding='utf-8-sig')
writer = csv.writer(file)

# Write each line to the CSV
headers = ["Region", "Cases"]
writer.writerow(headers)
for d in data:
  row = [d[0], d[1]]
  writer.writerow(row)