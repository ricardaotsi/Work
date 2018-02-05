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
    pyautogui.click(88, 258)
    pyautogui.PAUSE = 0.2
    pyautogui.click(140, 288); pyautogui.typewrite(line[0])#Name
    pyautogui.PAUSE
    pyautogui.click(140, 345); pyautogui.typewrite(line[1])#ID
    pyautogui.PAUSE
    pyautogui.click(140, 374); pyautogui.typewrite(line[2])#TIcket
    pyautogui.PAUSE
    pyautogui.click(500, 345); pyautogui.typewrite(line[3])#Type
    #Tab Company
    pyautogui.click(370, 255)
    pyautogui.click(397, 288)#Button serach company
    pyautogui.PAUSE
    pyautogui.press('enter')#enter to search company
    pyautogui.PAUSE = 0.3#delay to search
    pyautogui.click(466, 345)#Select company
    pyautogui.click(466, 345)#Select company
    #Tab Access Level
    pyautogui.click(513, 257)
    pyautogui.click(309, 290)#Button search access Level
    pyautogui.press('enter')#enter to search access Level
    pyautogui.PAUSE = 0.5#delay to search
    pyautogui.click(379, 325)#Select access Level (379/345 servidor)(379/364 terceirizado)(379,325 aluno)
    pyautogui.PAUSE = 0.5
    pyautogui.click(353, 287)#Add selection
    pyautogui.PAUSE = 0.5
    #Button save
    pyautogui.click(163, 619)
    pyautogui.PAUSE = 0.5#delay to save
    #Button confirmation
    pyautogui.click(634, 599)
    pyautogui.PAUSE = 0.6
# while True:
#         x, y = pyautogui.position()
#         print('X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4))
