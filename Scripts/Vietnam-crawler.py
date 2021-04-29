'''
@Author: Matthew Shabet
@Date: 2020-09-01 21:51:00
@LastEditTime: 2020-09-01 22:48:00
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
'''
import csv
import requests
import os
from datetime import datetime
from bs4 import BeautifulSoup
import json
begin_time = datetime.now()
url = "https://ncov.moh.gov.vn/"

hc_key = {
	"22": "Quảng Ninh",
	"56": "Khánh Hòa",
	"82": "Tiền Giang",
	"77": "Bà Rịa - Vũng Tàu",
	"60": "Bình Thuận",
	"79": "Hồ Chí Minh",
	"83": "Bến Tre",
	"94": "Sóc Trăng",
	"25": "Phú Thọ",
	"15": "Yên Bái",
	"30": "Hải Dương",
	"27": "Bắc Ninh",
	"33": "Hưng Yên",
	"37": "Ninh Bình",
	"35": "Hà Nam",
	"17": "Hòa Bình",
	"26": "Vĩnh Phúc",
	"01": "Hà Nội",
	"24": "Bắc Giang",
	"34": "Thái Bình",
	"68": "Lâm Đồng",
	"70": "Bình Phước",
	"54": "Phú Yên",
	"52": "Bình Định",
	"64": "Gia Lai",
	"51": "Quảng Ngãi",
	"87": "Đồng Tháp",
	"80": "Long An",
	"31": "Hải Phòng",
	"93": "Hậu Giang",
	"95": "Bạc Liêu",
	"86": "Vĩnh Long",
	"72": "Tây Ninh",
	"19": "Thái Nguyên",
	"12": "Lai Châu",
	"14": "Sơn La",
	"02": "Hà Giang",
	"36": "Nam Định",
	"42": "Hà Tĩnh",
	"40": "Nghệ An",
	"44": "Quảng Bình",
	"66": "Đắk Lắk",
	"58": "Ninh Thuận",
	"67": "Đắk Nông",
	"62": "Kon Tum",
	"49": "Quảng Nam",
	"45": "Quảng Trị",
	"46": "Thừa Thiên Huế",
	"48": "Đà Nẵng",
	"89": "An Giang",
	"96": "Cà Mau",
	"84": "Trà Vinh",
	"04": "Cao Bằng",
	"91": "Kiên Giang",
	"10": "Lào Cai",
	"11": "Điện Biên",
	"20": "Lạng Sơn",
	"38": "Thanh Hóa",
	"08": "Tuyên Quang",
	"74": "Bình Dương",
	"92": "Cần Thơ",
	"hs01": "Hoàng Sa",
	"truongsa": "Trường Sa"
}

# Get the data
response = requests.get(url, headers={'Connection': 'close'}, verify=False)
soup = BeautifulSoup(response.content, 'lxml')
script = soup.findAll("script")
index = [i for i in range(len(script)) if (str(script[i]).find("hc-key") >= 0)][0]
script = script[index].contents[0]
s = script.index("[", 1)
e = script.index("]") + 1
data = json.loads(script[s:e])

# Create and open the CSV
mkfile_time = datetime.strftime(datetime.now(), '%Y%m%d%H%M')
folder_path = './data/Vietnam/'+ mkfile_time + '/'
if not os.path.exists(folder_path):
	os.makedirs(folder_path)
file = open(folder_path+'table.csv', 'w', newline='', encoding='utf-8-sig')
writer = csv.writer(file)

headers = ["Region", "Infection", "Rehabilitate", "Dead"]
writer.writerow(headers)
for d in data:
	if (d["hc-key"] == "75"):
		continue
	row = [hc_key[d["hc-key"]], d["value"], d["socakhoi"], d["socatuvong"]]
	writer.writerow(row)

print(datetime.now() - begin_time)