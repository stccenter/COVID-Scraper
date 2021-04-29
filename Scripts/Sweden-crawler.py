'''
@Author: Matthew Shabet
@Date: 2020-09-11 18:00:00
@LastEditTime: 2020-09-11 18:30:00
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
'''
import csv
import requests
import os
import json
from datetime import datetime

url = 'https://services5.arcgis.com/fsYDFeRKu1hELJJs/arcgis/rest/services/FOHM_Covid_19_FME_1/FeatureServer/0/query?f=json&where=Region%20%3C%3E%20%27dummy%27&returnGeometry=false&spatialRel=esriSpatialRelIntersects&outFields=*&outSR=102100&resultOffset=0&resultRecordCount=25&resultType=standard&cacheHint=true'

# Get the data
response = requests.get(url, headers={'Connection': 'close'})
data = json.loads(response.text)["features"]

# Create and open the CSV
mkfile_time = datetime.strftime(datetime.now(), '%Y%m%d%H%M')
folder_path = './data/Sweden/'+ mkfile_time + '/'
if not os.path.exists(folder_path):
    os.makedirs(folder_path)
file = open(folder_path+'table.csv', 'w', newline='', encoding='utf-8-sig')
writer = csv.writer(file)

# Write each line to the csv
headers = ["Region", "Cases", "Cases/100k pop.", "Deaths", "Intensive care"]
writer.writerow(headers)
for d in data:
	d = d["attributes"] 
	row = [d["Region"], d["Totalt_antal_fall"], d["Fall_per_100000_inv"], d["Totalt_antal_avlidna"], d["Totalt_antal_intensivvårdade"]]
	writer.writerow(row)