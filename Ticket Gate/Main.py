import pyautogui
import csv

pyautogui.FAILSAFE = True

path = '/home/ti/Downloads/'
file=open( path +"velti.csv", "r")
reader = csv.reader(file)
for line in reader:
    #Tab personal data
    pyautogui.click(88, 258)
    pyautogui.click(140, 288); pyautogui.typewrite(line[0])#Name
    pyautogui.PAUSE
    pyautogui.click(140, 345); pyautogui.typewrite(line[2])#ID
    pyautogui.PAUSE
    pyautogui.click(140, 374); pyautogui.typewrite(line[5])#TIcket
    pyautogui.PAUSE
    pyautogui.click(500, 345); pyautogui.typewrite('Tecnico')#Type
    pyautogui.PAUSE
    #Tab Company
    pyautogui.click(370, 255)
    pyautogui.click(397, 288)#Button serach company
    pyautogui.press('enter')#enter to search company
    pyautogui.PAUSE = 0.4#delay to search
    pyautogui.click(466, 345)#Select company
    pyautogui.click(466, 345)#Select company
    #Tab Access Level
    pyautogui.click(513, 257)
    pyautogui.click(309, 290)#Button search access Level
    pyautogui.press('enter')#enter to search access Level
    pyautogui.PAUSE = 0.4#delay to search
    pyautogui.click(379, 345)#Select access Level
    pyautogui.click(353, 287)#Add selection
    #Button save
    pyautogui.click(163, 619)
    pyautogui.PAUSE = 0.4#delay to save
    #Button confirmation
    pyautogui.click(634, 599)
    pyautogui.PAUSE = 0.25#delay after confirmation
