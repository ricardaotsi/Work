import csv
import tkinter as tk
from tkinter import filedialog
import PyPDF2

#Create and hide window, only need an open file dialog
window = tk.Tk()
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
for value in data:
    if any(c in value for c in ('Série:','ZE', 'ZD', 'Z7', 'Z9', 'Produção (')):
        data_filter.append(next(data))
data_filter = zip(*[iter(data_filter)]*3)

#print the data to an organized csv file for later use
save_path=filedialog.asksaveasfilename( defaultextension=".csv")
csv=csv.writer(open(save_path,'w'))
for value in data_filter:
    csv.writerow(value)