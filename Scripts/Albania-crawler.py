'''
@Author: Matthew Shabet
@Date: 2020-08-02 21:51:00
@LastEditTime: 2020-08-02 22:48:00
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
'''
import csv
import requests
import json
import os
from datetime import datetime
begin_time = datetime.now()
url = 'https://coronavirus.al/api/qarqet.php'

# Get the data
response = requests.get(url, headers={'Connection': 'close'})
data = json.loads(response.text)

# Create and open the CSV
mkfile_time = datetime.strftime(datetime.now(), '%Y%m%d%H%M')
folder_path = './data/Albania/'+ mkfile_time + '/'
if not os.path.exists(folder_path):
    os.makedirs(folder_path)
file = open(folder_path+'table.csv', 'w', newline='', encoding='utf-8-sig')
writer = csv.writer(file)

headers = ["Region", "Total cases", "Recovered", "Deaths", "Active", "Intensive care", "Hospital treatment", "Home isolated", "Total tests"]
writer.writerow(headers)
for d in data:
  row = [d["qarku"], d["raste_gjithsej"], d["sheruar"], d["vdekur"], d["akt_pozitive"], d["terapi_int"], d["mjekim_spitalor"], d["izolim"], d["teste"]]
  writer.writerow(row)

print(datetime.now() - begin_time)
