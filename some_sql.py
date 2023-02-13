import requests
import json

all_data = json.loads(requests.get("<SOME_URL>").text)["data"]

# Writing to file
with open("myfile.sql", "w", encoding='utf8') as file1:
    for data in all_data:
        if "floor" in data and data["floor"] in stock_exchange_company:
            code = data["code"].replace("'","")
            shortName = data["shortName"].replace("'","") if "shortName" in data else ""
            companyNameEng = data["companyNameEng"].replace("'","")
            file1.write(f"INSERT INTO stock_name (code, name, name_english) VALUES('{code}', '{shortName}', '{companyNameEng}') ON DUPLICATE KEY UPDATE name_english=VALUES(name_english);\r\n")
