'''
@Author: Matthew Shabet
@Date: 2020-09-03 21:51:00
@LastEditTime: 2020-09-03 22:48:00
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
'''
import csv
import requests
import json
import os
from datetime import datetime

url = 'https://www.mohfw.gov.in/data/datanew.json'

# Get the data
response = requests.get(url, headers={'Connection': 'close'})
data = json.loads(response.text)

# Create and open the CSV
mkfile_time = datetime.strftime(datetime.now(), '%Y%m%d%H%M')
folder_path = './data/India/'+ mkfile_time + '/'
if not os.path.exists(folder_path):
    os.makedirs(folder_path)
file = open(folder_path+'table.csv', 'w', newline='', encoding='utf-8-sig')
writer = csv.writer(file)

# Write each line to the CSV
headers = ["state_name", "active", "positive", "cured", "death", "new_active", "new_positive", "new_cured", "new_death"]
writer.writerow(headers)
for d in data:
  row = [d[h] for h in headers]
  writer.writerow(row)