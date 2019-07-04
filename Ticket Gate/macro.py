import webbrowser
import pyautogui
import time

pyautogui.FAILSAFE = True
pyautogui.PAUSE=0.5

def buscar(i):
    pyautogui.click(674, 389)
    pyautogui.click(957, 384)
    pyautogui.typewrite(i)
    pyautogui.click(806, 472)

inp0 = input("Nome para Cadastrar: ")
inp1 = input("Cartão para Cadastrar: ")
inp2 = input("Matricula para cadastrar: ")

for i in range(4):
    webbrowser.open_new_tab('http://172.17.150.'+str(i+1)+'/')
    time.sleep(2)
    pyautogui.click(988, 322)
    pyautogui.click(723, 240)
    if not inp0:
        buscar(inp2)
    else:
        pyautogui.click(611, 391)
        pyautogui.click(836, 350)
        pyautogui.typewrite(inp0)
        pyautogui.click(839, 385)
        pyautogui.typewrite(inp2)
        pyautogui.click(855, 547)
        pyautogui.click(904, 621)
    pyautogui.click(843, 422,clicks=2)
    pyautogui.typewrite(inp1)
    pyautogui.click(689, 913)