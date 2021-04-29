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
import json
from datetime import datetime
begin_time = datetime.now()

# Create the directory
mkfile_time = datetime.strftime(datetime.now(), '%Y%m%d%H%M')
folder_path = './data/Bangladesh/'+ mkfile_time + '/'
if not os.path.exists(folder_path):
    os.makedirs(folder_path)


# The data in this site is actually split across three different sources
url = 'http://covid19tracker.gov.bd/'


# First, get the data for the entire country
url = 'http://covid19tracker.gov.bd/api/points'
response = requests.get(url, headers={'Connection': 'close'})
features = json.loads(response.text)["features"]
data = [f["properties"] for f in features if f["id"] == 'BGD'][0]

file = open(folder_path+'country.csv', 'w', newline='', encoding='utf-8-sig')
writer = csv.writer(file)

labels = ["Name", "LocalName", "TotalCases", "NewCases", "ActiveCases", "TotalRecovered", "NewRecovered", "TotalDeaths", "NewDeaths", "TotalTests", "RationPerMillion"]
writer.writerow(labels)
row = [data["name"], data["bnName"], data["TotalCases"], data["NewCases"], data["ActiveCases"], data["TotalRecovered"], data["NewRecovered"], data["TotalDeaths"], data["NewDeaths"], data["TotalTests"], data["RationPerMillion"]]
writer.writerow(row)


# Second, get the data for the major regions
url = 'https://covid19bangladesh.pythonanywhere.com/district'
response = requests.get(url, headers={'Connection': 'close'})
features = json.loads(response.text)["features"]
data = [f["properties"] for f in features]

file = open(folder_path+'regions.csv', 'w', newline='', encoding='utf-8-sig')
writer = csv.writer(file)

labels = ["Region", "LocalName", "ConfirmedCases"]
writer.writerow(labels)
for d in data:
  row = [d["name"], d["bnName"], d["confirmed"]]
  writer.writerow(row)


# Finally, get the data for the districts of Dhaka
url = 'https://covid19bangladesh.pythonanywhere.com/dhaka'
response = requests.get(url, headers={'Connection': 'close'})
data = json.loads(response.text)

file = open(folder_path+'dhaka.csv', 'w', newline='', encoding='utf-8-sig')
writer = csv.writer(file)

labels = ["Region", "LocalName", "ConfirmedCases"]
writer.writerow(labels)
for d in data:
  row = [d["name"], d["bnName"], d["confirmed"]]
  writer.writerow(row)

print(datetime.now() - begin_time)