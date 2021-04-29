'''
@Author: Matthew Shabet
@Date: 2020-07-31 23:30:00
@LastEditTime: 2020-08-1 02:52:00
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
'''
import ast
import csv
import requests
from urllib import request
from bs4 import BeautifulSoup
import os
from datetime import datetime
begin_time = datetime.now()
names = {
  "ភ្នំពេញ": "Phnom Penh",
  "ព្រះសីហនុ": "Sihanoukville",
  "កំពង់ចាម": "Kampong Cham",
  "បាត់ដំបង": "Battambang",
  "សៀមរាប": "Siem Reap",
  "បន្ទាយមានជ័យ": "Banteay Meanchey",
  "កែប": "Kep",
  "ត្បូងឃ្មុំ": "Tbong Khmum",
  "កំពង់ឆ្នាំង": "Krong Kampong Chhnang",
  "កណ្ដាល": "Kandal",
  "កោះកុង": "Koh Kong",
  "កំពត": "Krong Kampot",
  "ព្រះវិហារ": "Preah Vihear",
  "កំពង់ស្ពឺ": "Kampong Speu",
  "ប៉ៃលិន": "Pailin",
  "កំពង់ធំ": "Kampong Thom",
  "ស្វាយរៀង": "Svay Rieng",
  "ឧត្ដរមានជ័យ": "Oddor Meanchey",
  "ព្រៃវែង": "Prey Veng",
  "ប្រទេសកម្ពុជា": "Cambodia (totals)"
}

url = 'https://covid19-map.cdcmoh.gov.kh'

# Get the tag with the data
response = requests.get(url, headers={'Connection': 'close'})
soup = BeautifulSoup(response.content, 'lxml')
tag = soup.select('div[data-covid-19]')[0]

# `tag` has two attributes with important information
# `data` holds the numbers by region, while `summary` holds the country total
data = tag.get('data-covid-19')
summary = tag.get('data-summary')

# Clean and merge the data
summary = summary.replace("null","None")
summary = ast.literal_eval(summary)
data = data.replace("null","None")
data = ast.literal_eval(data)
data.append(summary)

# Create and open the CSV
mkfile_time = datetime.strftime(datetime.now(), '%Y%m%d%H%M')
folder_path = './data/Cambodia/'+ mkfile_time + '/'
if not os.path.exists(folder_path):
    os.makedirs(folder_path)
file = open(folder_path+'table.csv', 'w', newline='', encoding='utf-8-sig')
writer = csv.writer(file)


# Write each line to the CSV
labels = ["Region", "LocalName", "TotalCases", "NewCases", "Recoveries", "NewRecoveries", "Deaths", "NewDeaths"]
writer.writerow(labels)
for region in data:
    local_name = region["location"]["name_km"]
    row = [names[local_name], local_name, region["total_case"], region["new_case"], region["recovered_case"], region["new_recovered_case"], region["death_case"], region["new_death_case"]]
    writer.writerow(row)

print(datetime.now() - begin_time)

