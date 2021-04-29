'''
@Author: Matthew Shabet
@Date: 2020-08-12 14:00:00
@LastEditTime: 2020-08-12 14:55:00
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
'''
import csv
import requests
import os
from datetime import datetime
import json


#url = 'https://covid19honduras.org/'
# Actually get the data from here:
url = 'https://covid19honduras.org/dll/OMUERTOS_DEPTO.php'

# Get the data
response = requests.get(url, headers={'Connection': 'close'}, verify=False)
data = json.loads(response.text)

# Create the directory
mkfile_time = datetime.strftime(datetime.now(), '%Y%m%d%H%M')
folder_path = './data/Honduras/' + mkfile_time + '/'
if not os.path.exists(folder_path):
    os.makedirs(folder_path)
file = open(folder_path+'table.csv', 'w', newline='', encoding='utf-8-sig')
writer = csv.writer(file)

# Write each line to the CSV
labels = ["Region", "Infections", "Recovered", "Deaths"]
writer.writerow(labels)

for d in data:
    row = [d["name"], d["value"], d["recu"], d["muertos"]]
    writer.writerow(row)
