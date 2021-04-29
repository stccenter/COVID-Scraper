'''
@Author: Matthew Shabet
@Date: 2020-08-30 21:51:00
@LastEditTime: 2020-08-30 22:48:00
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
'''
import csv
import requests
import os
from datetime import datetime
from bs4 import BeautifulSoup

translate = {
	"denominazione_regione": "Region",
	"ricoverati_con_sintomi": "Hospitalized with symptoms",
	"terapia_intensiva": "Intensive care",
	"totale_ospedalizzati": "Total hospitalized",
	"isolamento_domiciliare": "Home isolated",
	"totale_positivi": "Total positives",
	"dimessi_guariti": "Healed/Discharged",
	"deceduti": "Deceased",
	"casi_da_sospetto_diagnostico": "Cases of diagnostic suspicion",
	"casi_da_screening": "Cases from screening",
	"totale_casi": "Total cases",
	"casi_testati": "Tested cases"
}

url = "https://github.com/pcm-dpc/COVID-19/blob/master/dati-regioni/dpc-covid19-ita-regioni-latest.csv"

# Get the data
response = requests.get(url, headers={'Connection': 'close'})
soup = BeautifulSoup(response.content, 'lxml')
tag = soup.findAll("table", {"class": "js-csv-data csv-data js-file-line-container"})[0]

# Create and open the CSV
mkfile_time = datetime.strftime(datetime.now(), '%Y%m%d%H%M')
folder_path = './data/Italy/'+ mkfile_time + '/'
if not os.path.exists(folder_path):
    os.makedirs(folder_path)
file = open(folder_path+'table.csv', 'w', newline='', encoding='utf-8-sig')
writer = csv.writer(file)

# Write the headers
head = tag.findAll("thead")[0]
headers = head.findAll("th")
headers = [h.contents[0] for h in headers][:-1]
mask = [3, 6, 7, 8, 9, 10, 13, 14, 15, 16, 17, 19]
headers = [translate[headers[m]] for m in mask]
writer.writerow(headers)

# Write each line to the CSV
table = tag.findAll("tbody")[0]
data = table.findAll("tr")
for d in data:
	nums = d.findAll("td")[1:-1]
	nums = [nums[m] for m in mask]
	row = [n.text for n in nums]
	writer.writerow(row)