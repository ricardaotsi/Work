import webbrowser
import pyautogui
import time

pyautogui.FAILSAFE = True
pyautogui.PAUSE=0.5

def buscar(i):
    pyautogui.click(723, 240)
    pyautogui.click(674, 389)
    pyautogui.click(957, 384)
    pyautogui.typewrite(i)
    pyautogui.click(806, 472)

inp1 = input("Cartão para Cadastrar: ")
inp2 = input("Matricula para cadastrar: ")

for i in range(4):
    webbrowser.open_new_tab('http://172.17.150.'+str(i+1)+'/')
    time.sleep(2)
    pyautogui.click(988, 322)
    buscar(inp2)
    pyautogui.click(843, 422,clicks=2)
    pyautogui.typewrite(inp1)
    pyautogui.click(694, 920)