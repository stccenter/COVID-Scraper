'''
@Author: Matthew Shabet
@Date: 2020-08-21 01:30:00
@LastEditTime: 2020-08-21 02:52:00
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
'''
import json
import csv
import requests
import os
from datetime import datetime

url = 'https://services9.arcgis.com/XPDxEtZ1oS0ENZZq/arcgis/rest/services/COVID_19_Ghana/FeatureServer/1/query?f=json&where=1%3D1&returnGeometry=false&spatialRel=esriSpatialRelIntersects&outFields=*&orderByFields=Number_of_Cases%20desc&resultOffset=0&resultRecordCount=25&resultType=standard&cacheHint=true'

response = requests.get(url, headers={'Connection': 'close'})
data = [d["attributes"] for d in json.loads(response.text)["features"]]

# Create and open the CSV
mkfile_time = datetime.strftime(datetime.now(), '%Y%m%d%H%M')
folder_path = './data/Ghana/'+ mkfile_time + '/'
if not os.path.exists(folder_path):
    os.makedirs(folder_path)
file = open(folder_path+'table.csv', 'w', newline='', encoding='utf-8-sig')
writer = csv.writer(file)

headers = ["REGION", "Number_of_Cases"]
writer.writerow(headers)
for d in data:
	row = [d[h] for h in headers]
	writer.writerow(row)