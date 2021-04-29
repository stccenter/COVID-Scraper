'''
@Author: Matthew Shabet
@Date: 2020-08-23 18:00:00
@LastEditTime: 2020-08-23 18:30:00
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
'''
import csv
import requests
import json
import os
from datetime import datetime

url = 'https://covid19.health.gov.mw:3000/api/v0/districts/aggregates'

# Get the data
response = requests.get(url, headers={'Connection': 'close'})
data = json.loads(response.text)["districts"]

# Create and open the CSV
mkfile_time = datetime.strftime(datetime.now(), '%Y%m%d%H%M')
folder_path = './data/Malawi/'+ mkfile_time + '/'
if not os.path.exists(folder_path):
    os.makedirs(folder_path)
file = open(folder_path+'table.csv', 'w', newline='', encoding='utf-8-sig')
writer = csv.writer(file)

# Write each line to the CSV
headers = ["districtName", "numberOfConfirmedCases", "numberOfConfirmedDeaths", "numberOfRecoveredPatients", "numberOfSuspectedCases"]
writer.writerow(headers)
for d in data:
	row = [d[h] for h in headers]
	writer.writerow(row)
