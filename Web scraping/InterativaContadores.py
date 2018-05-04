#!/usr/bin/python
import requests
from bs4 import BeautifulSoup
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import datetime

impressoras=["172.17.10.21",
            "172.17.10.22",
            "172.17.10.25",
            "172.17.10.26",
            "172.17.10.27",
            "172.17.10.28",
            "172.17.10.29",
            "172.17.10.30",
            "172.17.10.34"]

scope = ['https://spreadsheets.google.com/feeds']
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    "/path/to/json", scope)
gc = gspread.authorize(credentials)

sheet=1

for imp in impressoras:
    try:
        page1 = requests.get("http://"+imp+"/web/guest/br/websys/status/getUnificationCounter.cgi")
        page1.raise_for_status()
        soup = BeautifulSoup(page1.content, 'html5lib')
        contador=soup.find_all("tr", class_="staticProp")
        result_contador = list(contador[1])

        page2 = requests.get("http://"+imp+"/web/guest/br/webprinter/supply.cgi")
        page2.raise_for_status()
        soup = BeautifulSoup(page2.content,'html5lib')
        suprimento = soup.find_all("td", class_="black")
        result_suprimento = int((int(str(suprimento[0])[84:-8])*100)/162)

        gspreadlist = [
            datetime.datetime.now().strftime("%d/%m/%y %H:%M:%S"),
            str(result_contador[3])[14:-5],
            str(result_suprimento)+"%"
        ]

        wks = gc.open("Contadores").get_worksheet(sheet)
        wks.insert_row(gspreadlist, index=3)

        sheet += 1
    except requests.exceptions.RequestException as err:
        with open("/path/to/log", "a") as myfile:
            myfile.write(imp + " " + str(err) + "\n")