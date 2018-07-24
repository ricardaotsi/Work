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
result_suprimento_color = []
sheet = 1

scope = ['https://spreadsheets.google.com/feeds']
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    "/home/ti/Documentos/git/simpress-5e35fc2d6c71.json", scope)
gc = gspread.authorize(credentials)

for imp in impressoras:
    try:
        page1 = requests.get("http://"+imp+"/web/guest/br/websys/status/getUnificationCounter.cgi")
        page1.raise_for_status()
        page2 = requests.get("http://"+imp+"/web/guest/br/webprinter/supply.cgi")
        page2.raise_for_status()
    except requests.exceptions.RequestException as err:
        with open("/home/ti/Documentos/git/log", "a") as myfile:
            myfile.write(datetime.datetime.now().strftime("%d/%m/%y %H:%M:%S")+" : "+imp + " " + str(err) + "\n \n")
    else:
        soup = BeautifulSoup(page1.content, 'html5lib')
        contador = soup.find_all("tr", class_="staticProp")
        result_contador = list(contador[1])

        soup = BeautifulSoup(page2.content, 'html5lib')
        suprimento = soup.find_all("td", class_="black")
        result_suprimento = int((int(str(suprimento[0])[84:-8]) * 100) / 162)

        gspreadlist = [
            datetime.datetime.now().strftime("%d/%m/%y %H:%M:%S"),
            str(result_contador[3])[14:-5],
            str(result_suprimento) + "%"
        ]

        wks = gc.open("Contadores").get_worksheet(sheet)
        wks.insert_row(gspreadlist, index=3)

        with open("/home/ti/Documentos/git/log", "a") as myfile:
            myfile.write(datetime.datetime.now().strftime("%d/%m/%y %H:%M:%S")+" : "+imp+" DONE \n \n")

    sheet+=1

try:
    page3=requests.get("http://172.17.10.36/status/statgeneralx.htm")
    page3.raise_for_status()
    page4 = requests.get("http://172.17.10.36/status/statsuppliesx.htm")
    page4.raise_for_status()
except requests.exceptions.RequestException as err:
    with open("/home/ti/Documentos/git/log", "a") as myfile:
        myfile.write(datetime.datetime.now().strftime("%d/%m/%y %H:%M:%S") +
                     " : 172.17.10.36 " + str(err) + "\n \n")
else:
    soup = BeautifulSoup(page3.content, 'html5lib')
    contador = soup.find_all("td", class_="std_2")
    result_contador = str(contador[0])[18:-6]

    soup = BeautifulSoup(page4.content, 'html5lib')
    suprimento = soup.find_all("td", class_="stssupl_xog_3")
    for color in suprimento:
        result_suprimento_color.append(str(color)[26:-5])

    gspreadlist = [
        datetime.datetime.now().strftime("%d/%m/%y %H:%M:%S"), result_contador,
        result_suprimento_color[0], result_suprimento_color[1],
        result_suprimento_color[2], result_suprimento_color[3]
    ]

    wks = gc.open("Contadores").get_worksheet(10)
    wks.insert_row(gspreadlist, index=3)

    with open("/home/ti/Documentos/git/log", "a") as myfile:
        myfile.write(datetime.datetime.now().strftime("%d/%m/%y %H:%M:%S")+" : 172.17.10.36 DONE \n \n")

with open("/home/ti/Documentos/git/log", "a") as myfile:
    myfile.write("########################################################################## \n \n")
