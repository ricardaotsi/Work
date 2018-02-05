import pyautogui
import csv

pyautogui.FAILSAFE = True

path = '/home/ti/Downloads/'
file=open( path +"id.csv", "r")
reader = csv.reader(file)
for line in reader:
    pyautogui.click(200, 258); pyautogui.typewrite(line[0])#Numero Cracha
    pyautogui.PAUSE = 0.5
    pyautogui.click(400, 258); pyautogui.typewrite(line[0])#Numero Cracha
    pyautogui.PAUSE = 0.5
    pyautogui.click(200, 305) #Tipo Cracha
    pyautogui.PAUSE = 0.5
    pyautogui.click(200, 351) #Seleciona Tipo Cracha
    pyautogui.PAUSE = 0.5
    pyautogui.click(28,440) #local de trabalho
    pyautogui.PAUSE = 0.5
    pyautogui.click(120,600) #Salva
    pyautogui.PAUSE = 0.5
    pyautogui.click(639,601) #Salva
    pyautogui.PAUSE = 0.5
