'''
@Author: Matthew Shabet
@Date: 2020-09-08 21:51:00
LastEditTime: 2020-09-09 18:28:54
LastEditors: Please set LastEditors
@Description: In User Settings Edit
'''
import csv
import requests
import os
from datetime import datetime
from bs4 import BeautifulSoup
import json

translate = {
	'Москва': 'Moscow',
	'Московская область': 'Moscow Oblast',
	'Санкт-Петербург': 'Saint Petersburg',
	'Нижегородская область': 'Nizhegorodskaya Oblast',
	'Свердловская область': 'Sverdlov Oblast',
	'Ханты-Мансийский АО': 'Hanty-Mansiyskiy AO',
	'Ростовская область': 'Rostov Oblast',
	'Красноярский край': 'Krasnoyarskiy Kray',
	'Иркутская область': 'Irkutsk Oblast',
	'Воронежская область': 'Voronezh Oblast',
	'Челябинская область ': 'Cheliabinsk Oblast',
	'Ямало-Ненецкий автономный округ': 'Yamalo-Nenetskiy AO',
	'Мурманская область': 'Murmansk Oblast',
	'Саратовская область': 'Saratov Oblast',
	'Ставропольский край': 'Stavropolskiy Kray',
	'Волгоградская область': 'Volgograd Oblast',
	'Ульяновская область': 'Ulianovsk Oblast',
	'Алтайский край': 'Altayskiy Kray',
	'Краснодарский край': 'Krasnodarskiy Kray',
	'Новосибирская область': 'Novosibirsk Oblast',
	'Республика Дагестан': 'Republic of Dagestan',
	'Архангельская область': 'Arkhangelsk Oblast',
	'Оренбургская область': 'Orenburg Oblast',
	'Хабаровский край': 'Habarovskiy Kray',
	'Приморский край': 'Primorskiy Kray',
	'Омская область': 'Omsk Oblast',
	'Тульская область': 'Tula Oblast',
	'Самарская область': 'Samara Oblast',
	'Пензенская область': 'Pensa Oblast',
	'Брянская область': 'Briansk Oblast',
	'Калужская область': 'Kaluga Oblast',
	'Пермский край': 'Perm Oblast',
	'Тюменская область': 'Tumen Oblast',
	'Республика Башкортостан': 'Republic of Bashkortostan',
	'Республика Чувашия': 'Republic of Chuvashia',
	'Республика Саха (Якутия)': 'Saha Republic',
	'Ивановская область': 'Ivanovo Oblast',
	'Белгородская область': 'Belgorod Oblast',
	'Ярославская область': 'Yaroslavl Oblast',
	'Рязанская область': 'Ryazan Oblast',
	'Орловская область': 'Orel Oblast',
	'Курская область': 'Kursk Oblast',
	'Ленинградская область': 'Leningradskaya Oblast',
	'Кемеровская область': 'Kemerovo Oblast',
	'Республика Тыва': 'Republic of Tyva',
	'Кировская область': 'Kirov Oblast',
	'Тамбовская область': 'Tambov Oblast',
	'Республика Коми': 'Komi Republic',
	'Кабардино-Балкарская Республика': 'Republic of Kabardino-Balkaria',
	'Республика Татарстан': 'Republic of Tatarstan',
	'Владимирская область': 'Vladimir Oblast',
	'Смоленская область': 'Smolensk Oblast',
	'Томская область': 'Tomsk Oblast',
	'Астраханская область': 'Astrahan Oblast',
	'Республика Мордовия': 'Republic of Mordovia',
	'Тверская область': 'Tver Oblast',
	'Республика Бурятия': 'Republic of Buriatia',
	'Карачаево-Черкесская Республика': 'Republic of Karachaevo-Cherkessia',
	'Липецкая область': 'Lipetsk Oblast',
	'Республика Северная Осетия — Алания': 'Republic of North Osetia-Alania',
	'Забайкальский край': 'Zabaykalskiy Kray',
	'Псковская область': 'Pskov Oblast',
	'Республика Калмыкия': 'Republic of Kalmykia',
	'Сахалинская область': 'Sakhalin Oblast',
	'Республика Ингушетия': 'Ingushetia Republic',
	'Новгородская область': 'Novgorod Oblast',
	'Республика Марий Эл': 'Republic of Mariy El',
	'Камчатский край': 'Kamchatskiy Kray',
	'Костромская область': 'Kostroma Oblast',
	'Вологодская область': 'Vologda Oblast',
	'Амурская область': 'Amursk Oblast',
	'Республика Хакасия': 'Republic of Hakassia',
	'Калининградская область': 'Kaliningrad Oblast',
	'Республика Адыгея': 'Republic of Adygeia',
	'Удмуртская Республика': 'Republic of Udmurtia',
	'Республика Карелия': 'Republic of Karelia',
	'Курганская область': 'Kurgan Oblast',
	'Республика Крым': 'Republic of Crimea',
	'Чеченская Республика': 'Chechen Republic',
	'Республика Алтай': 'Altai Republic',
	'Магаданская область': 'Magadan Oblast',
	'Еврейская автономная область': 'Jewish Autonomous Oblast',
	'Севастополь': 'Sevastopol',
	'Ненецкий автономный округ': 'Nenetskiy Autonomous Oblast',
	'Чукотский автономный округ': 'Chukotskiy Autonomous Oblast'
}

url = "https://xn--80aesfpebagmfblc0a.xn--p1ai/information/"

# Get the data
response = requests.get(url, headers={'Connection': 'close'})
soup = BeautifulSoup(response.content, 'html.parser')
tag = soup.findAll("cv-spread-overview")[0][":spread-data"]
data = json.loads(tag)

# Create and open the CSV
mkfile_time = datetime.strftime(datetime.now(), '%Y%m%d%H%M')
folder_path = './data/Russia/'+ mkfile_time + '/'
if not os.path.exists(folder_path):
    os.makedirs(folder_path)
file = open(folder_path+'table.csv', 'w', newline='', encoding='utf-8-sig')
writer = csv.writer(file)

# Write each line to the CSV
headers = ["Region", "Local_name", "Sick", "Healed", "Deaths", "Sick_increase", "Healed_increase", "Deaths_increase"]
writer.writerow(headers)
for d in data:
	row = [translate[d["title"]], d["title"], d["sick"], d["healed"], d["died"], d["sick_incr"], d["healed_incr"], d["died_incr"]]
	writer.writerow(row)
print("Russia is done!")