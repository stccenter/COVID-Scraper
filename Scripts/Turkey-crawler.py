import os
import datetime
import tabula
import re
import requests
from bs4 import BeautifulSoup
from pathlib import Path
from datetime import datetime as dt

mkfile_time = dt.strftime(dt.now(), '%Y%m%d%H%M')
folder_path = './data/Turkey/' + mkfile_time + '/'
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

url = 'https://sbsgm.saglik.gov.tr/TR,66559/gunluk-rapor--daily-report.html'

regions = [
    'Istanbul', 'Western Marmara', 'Aegean', 'Eastern Marmara',
    'Western Anatolia', 'Mediterranean', 'Central Anatolia',
    'Western Blacksea', 'Eastern Blacksea', 'Northeastern Anatolia',
    'Mideastern Anatolia', 'Southeastern Anatolia'
]

html_txt = requests.get(url=url).text
soup = BeautifulSoup(html_txt, 'html.parser')
report_elems = soup.find_all('a', string=re.compile('Daily Situation Report'))
pdf_link = 'https://sbsgm.saglik.gov.tr/TR,77331/covid-19-daily-situation-report--23112020-eng.html'
match = re.search(r'(\d{2})(\d{2})(20\d{2})', pdf_link)
date = match.group(3) + '-' + match.group(2) + '-' + match.group(1)
file_name = date + '.csv'
if not file_name in folder_path:
    temp_file = folder_path + file_name + '_tmp'
    tabula.convert_into(pdf_link,
                        temp_file,
                        output_format="csv",
                        pages=3,
                        stream=True)
    temp_f = open(temp_file, 'r')
    f = open(folder_path + file_name, 'w')
    lines = temp_f.readlines()
    pattern = '(' + '|'.join(regions) + ')\s(\d+)'
    for line in lines:
        match = re.search(pattern, line)
        if match is not None:
            f.write(match.group(1) + ',' + match.group(2) + '\n')
    temp_f.close()
    f.close()

# clean temp files
for p in Path(folder_path).glob("*.csv_tmp"):
    p.unlink()
