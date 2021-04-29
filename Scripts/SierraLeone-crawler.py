'''
@Author: Matthew Shabet
@Date: 2020-08-17 15:00:00
@LastEditTime: 2020-08-17 16:17:00
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
'''
import ast
import csv
import requests
from bs4 import BeautifulSoup
import os
from datetime import datetime

url = 'http://dhse.gov.sl/'


# Make the directory
mkfile_time = datetime.strftime(datetime.now(), '%Y%m%d%H%M')
folder_path = './data/SierraLeone/'+ mkfile_time + '/'
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

eastern = ["Kailahun", "Kono", "Kenema"]
northern = ["Bombali", "Falaba", "Kambia", "Koinadugu", "Portloko", "Tonkolili"] 
southern = ["Bo", "Bonthe", "Moyamba", "Pujehun"]
western = ["Western Rural", "Western Urban"]

# Download the data
req = requests.get(url, headers={'Connection': 'close'}).content.decode('utf-8')

# Create the dictrict csv
file = open(folder_path+'districts.csv', 'w', newline='', encoding='utf-8-sig')
writer = csv.writer(file)
labels = ["District", "Confirmed Cases"]
writer.writerow(labels)

# Create the region csv
rfile = open(folder_path+'regions.csv', 'w', newline='', encoding='utf-8-sig')
rwriter = csv.writer(rfile)
rlabels = ["Eastern", "Northern", "Southern", "Western"]
rwriter.writerow(rlabels)

# Download the data
#requests.packages.urllib3.disable_warnings()
ecount = wcount = ncount = scount = 0
response = requests.get(url, headers={'Connection': 'close'})
soup = BeautifulSoup(response.content, 'lxml')
html_content = soup.findAll("div",{"class":"elementor-text-editor elementor-clearfix"})[19:55]

for i in range(0,len(html_content)-1,2):
	writer.writerow([html_content[i].text, html_content[i+1].text])
	if html_content[i].text in eastern:
		ecount += int(html_content[i+1].text)
	if html_content[i].text in western:
		wcount += int(html_content[i+1].text)
	if html_content[i].text in northern:
		ncount += int(html_content[i+1].text)
	if html_content[i].text in southern:
		scount += int(html_content[i+1].text)

rtotal = [ecount,wcount,ncount,scount]
rwriter.writerow(rtotal)
file.close()
rfile.close()