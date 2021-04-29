'''
@Author: Matthew Shabet
@Date: 2020-08-27 21:51:00
@LastEditTime: 2020-08-27 22:48:00
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
'''
import csv
import requests
import json
import os
from datetime import datetime


url = "https://api-covid19.rnbo.gov.ua/data?to=9999-12-31"


response = requests.get(url, headers={'Connection': 'close'})
data = json.loads(response.text)["ukraine"]

# Create and open the CSV
mkfile_time = datetime.strftime(datetime.now(), '%Y%m%d%H%M')
folder_path = './data/Ukraine/'+ mkfile_time + '/'
if not os.path.exists(folder_path):
    os.makedirs(folder_path)
file = open(folder_path+'table.csv', 'w', newline='', encoding='utf-8-sig')
writer = csv.writer(file)

# Write each line to the csv
headers = ["Region", "LocalName", "Confirmed", "Deaths", "Recovered", "Existing", "Suspected"]
writer.writerow(headers)
for d in data:
  row = [d["label"]["en"], d["label"]["uk"], d["confirmed"], d["deaths"], d["recovered"], d["existing"], d["suspicion"]]
  writer.writerow(row)