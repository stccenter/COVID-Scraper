'''
@Author: Matthew Shabet
@Date: 2020-08-26 21:51:00
@LastEditTime: 2020-09-25 22:48:00
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
'''
import csv
import requests
import json
import os
from datetime import datetime
begin_time = datetime.now()
translate = {
	"Region": "comunidad_autonoma",
	"Total cases": "casos_totales",
	"New cases": "nuevo_casos",
	"Diagnosed (last 24 hours)": "diagnosticados_ultimas_24_horas",
	"Diagnosed (last 7 days)": "diagnosticados_ultimos_7_dias",
	"% Cases": "%casos",
	"Diagnosed (last 14 days)": "diagnosticados_ultimos_14_dias",
	"Cumulative incidence": "ia",
	"Cumulative incidence (last 7 days)": "ia_7_dias",	
	"Deaths": "fallecidos",
	"Death increase": "incremento_fallecidos",
	"Deaths (last 7 days)": "fallecidos_ultimos_7_dias",
	"Recovered": "recuperados",
	"Hospitalized": "hospitalizados",
	"Percent hospitalized": "por_hospitalizados",
	"ICU": "uci",
	"Percent ICU": "por_uci",
	"PCR (last week)": "pcr_ultima_semana",
	"PCR per 100000 pop.": "pcr_100000_hab",
	"Percent positive": "por_positividad",
	"Risk assessment": "evaluacion_de_riesgo"
}

url = 'https://www.rtve.es/aplicaciones/infografias/rtve_2020/noticias/mapa-datosCCAA/territorios.json'

# Get the data
response = requests.get(url, headers={'Connection': 'close'})
data = json.loads(response.text)

# Create and open the CSV
mkfile_time = datetime.strftime(datetime.now(), '%Y%m%d%H%M')
folder_path = './data/Spain/'+ mkfile_time + '/'
if not os.path.exists(folder_path):
    os.makedirs(folder_path)
file = open(folder_path+'table.csv', 'w', newline='', encoding='utf-8-sig')
writer = csv.writer(file)

# Write each line to the CSV
headers = ["Region", "Total cases", "New cases", "Diagnosed (last 24 hours)", "Diagnosed (last 7 days)", "% Cases", "Diagnosed (last 14 days)", "Cumulative incidence", "Cumulative incidence (last 7 days)", "Deaths", "Death increase", "Deaths (last 7 days)", "Recovered", "Hospitalized", "Percent hospitalized", "ICU", "Percent ICU", "PCR (last week)", "PCR per 100000 pop.", "Percent positive", "Risk assessment"]
writer.writerow(headers)
for d in data:
    row = [d[translate[h]] for h in headers]
    writer.writerow(row)
print(datetime.now() - begin_time)