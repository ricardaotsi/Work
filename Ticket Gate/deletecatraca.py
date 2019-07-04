import pyautogui
import webbrowser
import time

pyautogui.FAILSAFE = True
pyautogui.PAUSE=0.5

listadelete = [18306145,	7112102,	19026934,	7102006,	7064545,	7106123,	7055207,	7112055,	7112161,	7112155,	7110092,	7109988,	7110052,	7118510,	7118509,	7118500,	19030772,	19021293,	19021370,	19027524,	19027435]

def buscar(i):
    pyautogui.click(674, 389)
    pyautogui.click(957, 384)
    pyautogui.typewrite(str(i))
    pyautogui.click(806, 472)

for i in range(4):
    webbrowser.open_new_tab('http://172.17.150.'+str(i+1)+'/')
    time.sleep(2)
    pyautogui.click(988, 322)
    for cartao in listadelete:
        pyautogui.click(723, 240)
        buscar(cartao)
        pyautogui.click(775, 915)
        time.sleep(1)
        
