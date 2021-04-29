'''
@Author: Matthew Shabet
@Date: 2020-07-31 23:30:00
@LastEditTime: 2020-08-1 02:52:00
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
'''
import json
import csv
import requests
import os
from datetime import datetime
begin_time = datetime.now()
#url = "https://dz-covid19.com/ws/?EIO=3&transport=polling"
url="https://api.corona-dz.live/province/latest"
response = requests.get(url, headers={'Connection': 'close'})
data = json.loads(response.text)

#url = url + "&sid=" + sid

#response = requests.get(url, headers={'Connection': 'close'}).text
#data = response[response.index("wilayas") + 9:-1]
#data = json.loads(data)

# Create and open the CSV
mkfile_time = datetime.strftime(datetime.now(), '%Y%m%d%H%M')
folder_path = './data/Algeria/'+ mkfile_time + '/'

if not os.path.exists(folder_path):
    os.makedirs(folder_path)
file = open(folder_path+'table.csv', 'w', newline='', encoding='utf-8-sig')
writer = csv.writer(file)

#headers = ["name", "confirmed", "deaths", "recovered", "active"]
headers = ["name", "confirmed", "deaths", "recovered"]
writer.writerow(headers)
for d in data:
	row = d["name"],d["data"][0]["confirmed"],d["data"][0]["deaths"],d["data"][0]["recovered"]
	writer.writerow(row)
print(datetime.now() - begin_time)