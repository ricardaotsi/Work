import csv
from tkinter import *
from tkinter import filedialog
import PyPDF2
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import locale
locale.setlocale(locale.LC_ALL, 'fr_FR.UTF-8')

#Create and hide window, only need an open file dialog
window = Tk()
window.withdraw()
open_path = filedialog.askopenfilename()

#get pdf from file_path and split text
pdf = PyPDF2.PdfFileReader(open(open_path, "rb"))
data_tmp = ''
for page in pdf.pages:
   data_tmp += page.extractText()
data = data_tmp.split('\n')

#filter the data to get what is needed and transform it in a nested list
data = iter(data)
data_filter=[]
date=0
for value in data:
    if any(c in value for c in ('Série:','ZE', 'ZD', 'Z7', 'Z9', 'Produção (')):
        data_filter.append(next(data).strip())
    if('Período' in value):
        date = next(data)
data_filter = list(zip(*[iter(data_filter)]*3))
month_ptBr = {1: 'janeiro', 2 : 'fevereiro', 3: 'março', 4: 'abril', 5: 'maio',
              6: 'junho', 7 : 'julho', 8: 'agosto', 9: 'setembro', 10: 'outubro',
              11: 'novembro', 12 : 'dezembro'}
day,month,year = date.split('/')
month=month_ptBr[int(month)]

#print the data to an organized csv file for later use
save_path=filedialog.asksaveasfilename( defaultextension=".csv")
csv=csv.writer(open(save_path,'w'))
for value in data_filter:
    csv.writerow(value)

#print the data to the desired google spreadsheet
oauth_path = filedialog.askopenfilename()
scope = ['https://spreadsheets.google.com/feeds']
credentials = ServiceAccountCredentials.from_json_keyfile_name(oauth_path, scope)
gc = gspread.authorize(credentials)
user_imput = Tk()
user_entry = Entry(user_imput)
user_entry.pack()
user_entry.focus_set()
def callback():
    user_entry.destroy()
user_button = Button(user_imput, text="Send", width=10, command=callback)
user_button.pack()
user_imput.mainloop()
#print copies in worksheet 1
wks = gc.open(user_entry.get()).get_worksheet(1)
sheet_month = wks.find(month)
for value in data_filter:
    sheet_serial = wks.find(value[0])
    wks.update_cell(sheet_serial.row, sheet_month.col, value[2])
#print price in worksheet 2
wks = gc.open(user_entry.get()).get_worksheet(2)
for value in data_filter:
    sheet_serial = wks.find(value[0])
    tmp = value[1].strip('R$ ')
    tmp = locale.format('%.2f', float(tmp))
    wks.update_cell(sheet_serial.row, sheet_month.col, tmp)
