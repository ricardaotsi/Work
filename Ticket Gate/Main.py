import pyautogui
import csv
from tkinter import *
from tkinter import filedialog

pyautogui.FAILSAFE = True

window = Tk()
window.withdraw()
open_path = filedialog.askopenfilename()
file=open( open_path, "r")
reader = csv.reader(file)
for line in reader:
    #Tab personal data
    pyautogui.click(77, 271)
    pyautogui.PAUSE = 0.2
    pyautogui.click(133, 304); pyautogui.typewrite(line[1])#Name
    pyautogui.PAUSE = 0.2
    pyautogui.click(136, 363); pyautogui.typewrite(line[0])#ID
    pyautogui.PAUSE = 0.2
    pyautogui.click(136, 390); pyautogui.typewrite(line[2])#TIcket
    pyautogui.PAUSE = 0.2
    pyautogui.click(519, 360); pyautogui.typewrite(line[3])#Type
    #Tab Company
    pyautogui.click(402, 271)
    pyautogui.click(400, 303)#Button serach company
    pyautogui.PAUSE = 0.3
    pyautogui.press('enter')#enter to search company
    pyautogui.PAUSE = 0.3#delay to search
    pyautogui.click(448, 364)#Select company
    pyautogui.click(448, 364)#Select company
    #Tab Access Level
    pyautogui.click(573, 267)
    pyautogui.click(320, 300)#Button search access Level
    pyautogui.press('enter')#enter to search access Level
    pyautogui.PAUSE = 0.4#delay to search
    pyautogui.click(379, 339)#Select access Level (379/360 servidor)(379/384 terceirizado)(379,339 aluno)
    pyautogui.PAUSE = 0.3
    pyautogui.click(359, 302)#Add selection
    pyautogui.PAUSE = 1.0
    #Button save
    pyautogui.click(140, 631)
    pyautogui.PAUSE = 0.5#delay to save
    #Button confirmation
    pyautogui.click(640, 609)
    pyautogui.PAUSE = 0.5
# while True:
#         x, y = pyautogui.position()
#         print('X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4))
