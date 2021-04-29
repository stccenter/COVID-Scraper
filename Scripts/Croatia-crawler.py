'''
@Author: Matthew Shabet
@Date: 2020-08-28 18:00:00
@LastEditTime: 2020-08-28 18:30:00
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
'''
import csv
import requests
import json
import os
from datetime import datetime
from bs4 import BeautifulSoup

# empty list
data = []

url = "https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Croatia"
response = requests.get(url, headers={'Connection': 'close'})
soup = BeautifulSoup(response.content, 'lxml')
html_content = soup.find("table",{"class":"wikitable"}).find_all("tr")[1:22]

headers = ["Region", "Cases", "Deaths", "Active"]

# Create and open the CSV
mkfile_time = datetime.strftime(datetime.now(), '%Y%m%d%H%M')
folder_path = './data/Croatia/'+ mkfile_time + '/'
if not os.path.exists(folder_path):
    os.makedirs(folder_path)
file = open(folder_path+'table.csv', 'w', newline='', encoding='utf-8-sig')
writer = csv.writer(file)
writer.writerow(headers)

for each_row in html_content:
    sub_data = []
    links = each_row.find('a', href=True)
    try:
        title = links.attrs['title']
        sub_data.append(title)
    except AttributeError:
        pass

    for sub_element in each_row:
        try:
            sub_data.append(sub_element.get_text())
        except:
            continue
    data.append(sub_data)

for d in data:
    row = [d[0].strip('\n'),d[2].strip('\n'),d[4].strip('\n'),d[6].strip('\n')]
    writer.writerow(row)