'''
@Author: Matthew Shabet
@Date: 2020-09-04 21:51:00
LastEditTime: 2020-09-09 18:29:45
LastEditors: Please set LastEditors
@Description: In User Settings Edit
'''
import csv
import requests
import json
import os
from datetime import datetime
begin_time = datetime.now()


url = "https://xx9p7hp1p7.execute-api.us-east-1.amazonaws.com/prod/PortalRegiaoSaude"

# Get the data
response = requests.get(url, headers={'Connection': 'close'})
data = json.loads(response.text)

# Create and open the CSV
mkfile_time = datetime.strftime(datetime.now(), '%Y%m%d%H%M')
folder_path = './data/Brazil/'+ mkfile_time + '/'
if not os.path.exists(folder_path):
    os.makedirs(folder_path)
file = open(folder_path+'HealthRegion.csv', 'w', newline='', encoding='utf-8-sig')
writer = csv.writer(file)

# Write each line to the CSV
headers = ["Name", "Accumulated cases", "Accumulated deaths", "Incidence", "Death incidence"]
writer.writerow(headers)
for d in data:
  row = [d["nome"], d["casosAcumulado"], d["obitosAcumulado"], d["incidencia"], d["incidenciaObito"]]
  writer.writerow(row)



url = "https://xx9p7hp1p7.execute-api.us-east-1.amazonaws.com/prod/PortalMunicipio"

# Get the data
response = requests.get(url, headers={'Connection': 'close'})
data = json.loads(response.text)

# Create and open the CSV
file = open(folder_path+'Municipality.csv', 'w', newline='', encoding='utf-8-sig')
writer = csv.writer(file)

# Write each line to the CSV
headers = ["Name", "Accumulated cases", "Accumulated deaths"]
writer.writerow(headers)
for d in data:
  row = [d["nome"], d["casosAcumulado"], d["obitosAcumulado"]]
  writer.writerow(row)



url = "https://xx9p7hp1p7.execute-api.us-east-1.amazonaws.com/prod/PortalEstado"

# Get the data
response = requests.get(url, headers={'Connection': 'close'})
data = json.loads(response.text)

# Create and open the CSV
file = open(folder_path+'State.csv', 'w', newline='', encoding='utf-8-sig')
writer = csv.writer(file)

# Write each line to the CSV
headers = ["Name", "Accumulated cases", "Accumulated deaths", "TCU 2019 population", "Incidence", "Death incidence"]
writer.writerow(headers)
for d in data:
  row = [d["nome"], d["casosAcumulado"], d["obitosAcumulado"], d["populacaoTCU2019"], d["incidencia"], d["incidenciaObito"]]
  writer.writerow(row)

print("Brazil is done!")
print(datetime.now() - begin_time)