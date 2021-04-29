'''
@Author: Matthew Shabet
@Date: 2020-08-25 17:00:00
@LastEditTime: 2020-08-25 18:30:00
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
'''
import csv
import requests
import os
from datetime import datetime
from bs4 import BeautifulSoup


url = 'https://github.com/iMEdD-Lab/open-data/blob/master/COVID-19/greece_latest.csv'

# empty list
data = []
# Get the data
response = requests.get(url, headers={'Connection': 'close'})

soup = BeautifulSoup(response.content, 'lxml')
HTML_data_header = soup.find_all("table")[0].find_all("th")
HTML_data = soup.find_all("table")[0].find_all("tr")[1:]

header=[]
for each_header in HTML_data_header:
    header.append(each_header.get_text())


# Write each line to the csv
headers = ["Region", "LocalName", "Cases", "Deaths"]

# Create and open the CSV
mkfile_time = datetime.strftime(datetime.now(), '%Y%m%d%H%M')
folder_path = './data/Greece/'+ mkfile_time + '/'
if not os.path.exists(folder_path):
    os.makedirs(folder_path)
file = open(folder_path+'table.csv', 'w', newline='', encoding='utf-8-sig')
writer = csv.writer(file)
writer.writerow([header[0],header[1],header[7],header[8]])


# for getting the data
for element in HTML_data:
    sub_data = []
    for sub_element in element:
        try:
            sub_data.append(sub_element.get_text())
        except:
            continue
    data.append(sub_data)


for d in data:
    row = [d[1],d[2],d[8],d[9]]
    writer.writerow(row)