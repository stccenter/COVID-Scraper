import os
import tabula
from pathlib import Path
import re
from datetime import datetime as dt
import datetime


districts = [
    'COLOMBO', 'GAMPAHA', 'PUTTALAM', 'KALUTARA', 'ANURADHAPURA', 'KANDY',
    'Kurunegala', 'JAFFNA', 'RATNAPURA', 'POLONNARUWA', 'KEGALLE',
    'MONERAGALA', 'KALMUNAI', 'MATALE', 'GALLE', 'BADULLA', 'MATARA',
    'BATTICOLOA', 'HAMBANTOTA', 'VAVUNIA', 'TRINCOMALEE', 'AMPARA',
    'NUWARAELIYA', 'KILINOCHCHI', 'MANNAR', 'MULLATIVU', 'TH Jaffna'
]
###

today = datetime.date.today()
curr_date_str = today.strftime('%Y-%m-%d')

mkfile_time = dt.strftime(dt.now(), '%Y%m%d%H%M')
#mkfile_time = today.strftime('%Y%m%d%H%M')
folder_path = './data/SriLanka/' + mkfile_time + '/'
if not os.path.exists(folder_path):
    os.makedirs(folder_path)


file_name = curr_date_str + '_tmp'
file_name1 = curr_date_str + '.csv'
pdf_link = 'https://www.epid.gov.lk/web/images/pdf/corona_virus_report/sitrep-sl-en-' + today.strftime(
    '%d') + '-' + today.strftime('%m') + '_10_' + today.strftime('%y') + '.pdf'
temp_file = folder_path + file_name + '.csv'
try:
    tabula.convert_into(pdf_link,
                        temp_file,
                        output_format="csv",
                        pages=1,
                        area=(331, 313, 613, 586))
    temp_f = open(temp_file, 'r')
    f = open(folder_path + file_name1, 'w')
    pattern = '|'.join([x for x in districts])
    pattern = '(' + pattern + ')(\d+)'
    lines = temp_f.readlines()
    for line in lines:
        new_line = re.sub(r'(\s|\n)', '', line)
        letters = re.sub(r'\d', '', new_line).replace(",", "")
        numbers = re.sub(r'[A-Za-z]', '', new_line).replace(",", "")
        match = re.search(pattern, letters + numbers)
        if match is not None:
            f.write(match.group(1) + ',' + match.group(2) + '\n')
    temp_f.close()
    f.close()
except:
    print('Cannot parse Sri Lanka data for ' + curr_date_str)

# clean temp files
for p in Path(folder_path).glob("*_tmp.csv"):
    p.unlink()
