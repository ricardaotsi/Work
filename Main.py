import csv
from tkinter import *
from tkinter import filedialog

window = Tk()
window.withdraw()
open_path = filedialog.askopenfilename()
fileo=open( open_path, "r")
save_path = filedialog.askopenfilename()
files=open( save_path, "w")
reader = csv.reader(fileo)
for line in reader:
    files.write("\nhost "+line[0]+"{\n")
    files.write("\thardware ethernet "+line[1]+";\n")
    files.write("\tfixed-address "+line[2]+";\n")
    files.write("}\n")
