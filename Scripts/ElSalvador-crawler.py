'''
@Author: Matthew Shabet
@Date: 2020-08-16 09:00:00
@LastEditTime: 2020-08-16 14:00:00
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
'''
import csv
import requests
from bs4 import BeautifulSoup
import os
from datetime import datetime
import json

url = 'https://covid19.gob.sv'
# Actually get the data from here
url = 'https://e.infogram.com/_/fx5xud0FhM7Z9NS6qpxs?v=1?parent_url=https%3A%2F%2Fcovid19.gob.sv%2F&src=embed#async_embed'

# Get the tag with the data
response = requests.get(url, headers={'Connection': 'close'})
soup = BeautifulSoup(response.content, 'lxml')
string = soup.find_all("script")[4].string[23:-1]
data = json.loads(string)["elements"]["content"]["content"]["entities"]

# Make the folder
mkfile_time = datetime.strftime(datetime.now(), '%Y%m%d%H%M')
folder_path = './data/ElSalvador/'+ mkfile_time + '/'
if not os.path.exists(folder_path):
    os.makedirs(folder_path)


# Country
magicnumbers = ["f47481c2-a324-46bb-9357-5844973345cd", "02efa09c-df92-4488-9673-421b11745610", "f4389629-ddf5-4d4e-bf15-3d6f28605dbc", "4e150f58-b52b-47a1-bc62-20e2f5f31da1", "39288631-6c95-48ef-a67c-15b24c9adf70"]
file = open(folder_path+'country.csv', 'w', newline='', encoding='utf-8-sig')
writer = csv.writer(file)
labels = ["Confirmed", "Active", "Recovered", "Deaths", "Tests"]
writer.writerow(labels)
row = [data[n]["props"]["content"]["blocks"][0]["text"] for n in magicnumbers]
writer.writerow(row)


# Regions
regions = data["91478eeb-c7bf-4b3f-a9f4-c2340226a820"]["props"]["chartData"]["data"][0][1:]
file = open(folder_path+'regions.csv', 'w', newline='', encoding='utf-8-sig')
writer = csv.writer(file)
labels = ["Region", "ConfirmedCases"]
writer.writerow(labels)
for r in regions:
  row = [r[0], r[1]]
  writer.writerow(row)


# Cities
regions = [["SAN SALVADOR", data["0145be48-e77d-41f9-8660-9fdddb338fb4"]["props"]["chartData"]["data"][0][1:20]],
["LA LIBERTAD", data["6c6fc20e-292b-4f4a-9c98-ed1c52acf8c2"]["props"]["chartData"]["data"][0][1:]],
["SANTA ANA", data["74f80e2b-3270-44e7-a670-c77201102327"]["props"]["chartData"]["data"][0][1:13]],
["SAN MIGUEL", data["1beedbfd-d146-4d3b-92c3-fea680b1cc0d"]["props"]["chartData"]["data"][0][1:19]],
["LA PAZ", data["ae286daa-cc89-4036-b961-87c99e193c0b"]["props"]["chartData"]["data"][0][1:23]],
["AHUACHAPÁN", data["d95b3e4b-5cd5-491c-9e4a-010b9f0dd252"]["props"]["chartData"]["data"][0][1:13]],
["CUSCATLÁN", data["3a9da217-d898-40f4-8e78-c9c3391eb5fc"]["props"]["chartData"]["data"][0][1:16]],
["SONSONATE", data["c234ac87-73e6-408a-83ff-6aff64ce0b79"]["props"]["chartData"]["data"][0][1:17]],
["LA UNIÓN", data["e80e27fe-a72d-45ef-bba1-2bcf4af01a4b"]["props"]["chartData"]["data"][0][1:]],
["SAN VICENTE", data["8a129c87-3607-40d7-b09a-c96ff6215837"]["props"]["chartData"]["data"][0][1:14]],
["CHALATENANGO", data["17347c1e-f30b-4cfd-9cfe-bfb552153506"]["props"]["chartData"]["data"][0][1:30]],
["USULUTÁN", data["5e255f2d-f556-4c9b-988b-ab5cb0cd8eb9"]["props"]["chartData"]["data"][0][1:24]],
["CABAÑAS", data["f98e6253-4a0e-43be-842c-e67dea13ec81"]["props"]["chartData"]["data"][0][1:10]],
["MORAZÁN",data["9ec618b7-756c-40af-af85-0248b74f2ffd"]["props"]["chartData"]["data"][0][1:]]]

file = open(folder_path+'cities.csv', 'w', newline='', encoding='utf-8-sig')
writer = csv.writer(file)
labels = ["Municipality", "Region", "ConfirmedCases"]
writer.writerow(labels)
for region in regions:
  for city in region[1]:
    row = [city[0], region[0], city[1]]
    writer.writerow(row)