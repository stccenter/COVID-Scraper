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


url = 'https://covid19.moh.gov.om/ens/outbreak/getRegionWalayatSummary'

# Get the data
requests.packages.urllib3.disable_warnings()
response = requests.get(url, headers={'Connection': 'close'},verify=False)
data = json.loads(response.text)["result"]

# Create and open the CSV
mkfile_time = datetime.strftime(datetime.now(), '%Y%m%d%H%M')
folder_path = './data/Oman/'+ mkfile_time + '/'
if not os.path.exists(folder_path):
    os.makedirs(folder_path)
file = open(folder_path+'table.csv', 'w', newline='', encoding='utf-8-sig')
writer = csv.writer(file)

# Write each line to the CSV
headers = ["Region", "Confirmed", "Sick", "Recovered", "Deaths", "Suspected", "Quarantined"]
writer.writerow(headers)
for d in data:
  row = [d["regionName"], d["infected"], d["currentlySick"], d["recovered"], d["death"], d["suspected"], d["quarantined"]]
  writer.writerow(row)