'''
@Author: Matthew Shabet
@Date: 2020-08-13 13:30:00
@LastEditTime: 2020-08-13 14:33:00
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
'''
import ast
import csv
import requests
from bs4 import BeautifulSoup
import os
from datetime import datetime

names = {
    "جبل لبنان": "Mount Lebanon",
    "غير محدد": "Undefined",
    "بيروت": "Beirut",
    "الشمال": "North Lebanon",
    "الجنوب": "South Lebanon",
    "‫البقاع‬": "Beqaa",
    "النبطية": "Nabatieh",
    "بعلبك الهرمل": "Baalbek-Hermel",
    "عكار": "Aakkar"
}

url = 'https://corona.ministryinfo.gov.lb/'

# Retrieve the script that generates the data
response = requests.get(url, headers={'Connection': 'close'})
soup = BeautifulSoup(response.content, 'lxml')
string = soup.find_all("script")[22].string


# Pick out the case numbers
array = string[string.index("[", 100):string.index("]", 100) + 1]
data = ast.literal_eval(array)

# Pick out the region names
start = "cat_str.push('"
s = [i + len(start) for i in range(len(string)) if string.startswith(start, i)]
e = [i - 1 for i in range(len(string)) if string.startswith(');', i)]
regions = [string[s[i]:e[i]] for i in range(9)]

# Create and open the CSV
mkfile_time = datetime.strftime(datetime.now(), '%Y%m%d%H%M')
folder_path = './data/Lebanon/' + mkfile_time + '/'
if not os.path.exists(folder_path):
    os.makedirs(folder_path)
file = open(folder_path+'table.csv', 'w', newline='', encoding='utf-8-sig')
writer = csv.writer(file)

labels = ["Region", "LocalName", "TotalCases"]
writer.writerow(labels)
for (r, d) in zip(regions, data):
    row = [names[r], r, d]
    writer.writerow(row)
