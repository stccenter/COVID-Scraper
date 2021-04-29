'''
@Author: Matthew Shabet
@Date: 2020-11-12 19:51:00
@LastEditTime: 2020-11-15 23:48:00
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
'''
import csv
import requests
import os
from datetime import datetime
from bs4 import BeautifulSoup
import json

url = "https://www.gov.pl/web/koronawirus/wykaz-zarazen-koronawirusem-sars-cov-2"

response = requests.get(url, headers={'Connection': 'close'})
soup = BeautifulSoup(response.content, 'html.parser')
tag = soup.findAll("pre", {"class": "hide"})[0].text
data = json.loads(tag)["data"].split("\n")[1:-1]

# Create and open the CSV
mkfile_time = datetime.strftime(datetime.now(), '%Y%m%d%H%M')
folder_path = './data/Poland/'+ mkfile_time + '/'
if not os.path.exists(folder_path):
    os.makedirs(folder_path)
file = open(folder_path+'table.csv', 'w', newline='', encoding='utf-8-sig')
writer = csv.writer(file)

headers = ["Region", "Cases", "Deaths"]
writer.writerow(headers)
for d in data:
    row = d.split(";")[:3]
    writer.writerow(row)