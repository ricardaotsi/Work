#!/usr/bin/python
import requests
from bs4 import BeautifulSoup
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import datetime
import threading

impressoras=[["172.17.10.21", 1],
            ["172.17.10.22", 2],
            ["172.17.10.25", 3],
            ["172.17.10.26", 4],
            ["172.17.10.27", 5],
            ["172.17.10.28", 6],
            ["172.17.10.29", 7],
            ["172.17.10.30", 8],
            ["172.17.10.34", 9]]

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    "/home/infcuritiba/interativa/simpress-5e35fc2d6c71.json", scope)
gc = gspread.authorize(credentials)

log = "/home/infcuritiba/interativa/log"

def contadores(imp, sheet):
    try:
        page1 = requests.get("http://"+imp+"/web/guest/br/websys/status/getUnificationCounter.cgi")
        page1.raise_for_status()
    except requests.exceptions.RequestException as err:
        with open(log, "a") as myfile:
            myfile.write(datetime.datetime.now().strftime("%d/%m/%y %H:%M:%S")+" : "+imp + " " + str(err) + "\n \n")
    else:
        soup = BeautifulSoup(page1.content, 'html5lib')
        contador = soup.find_all("tr", class_="staticProp")
        result_contador = list(contador[1])
        
        gspreadlist = [
            datetime.datetime.now().strftime("%d/%m/%y %H:%M:%S"),
            str(result_contador[3])[14:-5]
        ]

        wks = gc.open("Contadores").get_worksheet(sheet)
        wks.insert_row(gspreadlist, index=3)

        with open(log, "a") as myfile:
            myfile.write(datetime.datetime.now().strftime("%d/%m/%y %H:%M:%S")+" : "+imp+" DONE \n \n")

for imp in impressoras:
    x = threading.Thread(target=contadores, args=(imp[0],imp[1]))
    x.start()

try:
    page3=requests.get("http://172.17.10.36/status/statgeneralx.htm")
    page3.raise_for_status()
except requests.exceptions.RequestException as err:
    with open(log, "a") as myfile:
        myfile.write(datetime.datetime.now().strftime("%d/%m/%y %H:%M:%S") +" : 172.17.10.36 " + str(err) + "\n \n")
else:
    soup = BeautifulSoup(page3.content, 'html5lib')
    contador = soup.find_all("td", class_="std_2")
    result_contador = str(contador[0])[18:-6]

    gspreadlist = [
        datetime.datetime.now().strftime("%d/%m/%y %H:%M:%S"), 
        result_contador
    ]

    wks = gc.open("Contadores").get_worksheet(10)
    wks.insert_row(gspreadlist, index=3)

    with open(log, "a") as myfile:
        myfile.write(datetime.datetime.now().strftime("%d/%m/%y %H:%M:%S")+" : 172.17.10.36 DONE \n \n")
