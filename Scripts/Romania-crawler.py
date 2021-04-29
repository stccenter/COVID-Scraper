'''
@Author: Matthew Shabet
@Date: 2020-08-22 20:00:00
@LastEditTime: 2020-08-22 21:30:00
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
'''
import csv
import requests
import os
from datetime import datetime
import json

translate = {
  "Region": "Judete",
  "ConfirmedCases": "Cazuri_confirmate",
  "Population": "Populatie",
  "Quarantined": "Persoane_in_carantina",
  "Isolated": "Persoane_izolate"
}

url = "https://services7.arcgis.com/I8e17MZtXFDX9vvT/arcgis/rest/services/Coronavirus_romania/FeatureServer/0/query?f=json&where=1%3D1&returnGeometry=false&spatialRel=esriSpatialRelIntersects&outFields=*&orderByFields=Cazuri_confirmate%20desc&resultOffset=0&resultRecordCount=45&resultType=standard&cacheHint=true"

response = requests.get(url, headers={'Connection': 'close'})
data = json.loads(response.text)["features"]

# Create and open the CSV
mkfile_time = datetime.strftime(datetime.now(), '%Y%m%d%H%M')
folder_path = './data/Romania/'+ mkfile_time + '/'
if not os.path.exists(folder_path):
    os.makedirs(folder_path)
file = open(folder_path+'table.csv', 'w', newline='', encoding='utf-8-sig')
writer = csv.writer(file)

# Write each line to the CSV
headers = ["Region", "ConfirmedCases", "Population", "Quarantined", "Isolated"]
writer.writerow(headers)
for d in data:
	d = d["attributes"]
	row = [d[translate[h]] for h in headers]
	writer.writerow(row)