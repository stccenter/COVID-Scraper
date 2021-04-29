'''
@Author: Matthew Shabet
@Date: 2020-08-31 21:51:00
LastEditTime: 2020-08-31 13:10:36
LastEditors: Please set LastEditors
@Description: In User Settings Edit
'''
import csv
import requests
import os
from datetime import datetime

url = 'https://data.gov.lv/dati/dataset/e150cc9a-27c1-4920-a6c2-d20d10469873/resource/492931dd-0012-46d7-b415-76fe0ec7c216/download/covid_19_pa_adm_terit.csv'

nregions = 120

# Get the data
response = requests.get(url, headers={'Connection': 'close'})
data = response.content.decode("utf-8").splitlines()[-nregions:]

# Create and open the CSV
mkfile_time = datetime.strftime(datetime.now(), '%Y%m%d%H%M')
folder_path = './data/Latvia/'+ mkfile_time + '/'
if not os.path.exists(folder_path):
    os.makedirs(folder_path)
file = open(folder_path+'table.csv', 'w', newline='', encoding='utf-8-sig')
writer = csv.writer(file)

# Write each line to the CSV
headers = ["Region", "Confirmed Cases", "Active cases"]
writer.writerow(headers)
for d in data:
	d = d.split(";")
	d = ["1" if v == "no 1 līdz 5" else v for v in d]
	row = [d[1], d[3], d[4]]
	writer.writerow(row)
print("Latvia is done!")