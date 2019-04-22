import webbrowser
import pyautogui
import time

pyautogui.FAILSAFE = True
#pyautogui.PAUSE=0.3

def alt_Tab():
    pyautogui.keyDown('alt')
    time.sleep(0.2)
    pyautogui.press('tab')
    time.sleep(0.2)
    pyautogui.keyUp('alt')
    time.sleep(2)

def buscar(i):
    pyautogui.click(702, 240)
    pyautogui.click(637, 389)
    pyautogui.click(926, 384)
    pyautogui.typewrite(i)
    time.sleep(0.5)
    pyautogui.click(772, 472)

inp1 = input("Cartão para Cadastrar: ")
inp2 = input("Matricula para cadastrar: ")

for i in range(4):
    webbrowser.open_new_tab('http://172.17.150.'+str(i+1)+'/')
    time.sleep(1)
    pyautogui.click(960, 335)
    time.sleep(2)
    buscar(inp1)
    alt_Tab()
    inp = input("Deseja excluir s/n ? ")
    if inp == 's':
        alt_Tab()
        time.sleep(2)
        pyautogui.click(751, 922)
        buscar(inp2)
        time.sleep(0.3)
        pyautogui.click(809, 422,clicks=2)
        pyautogui.typewrite(inp1)
        time.sleep(0.5)
    elif inp == 'n':
        alt_Tab()
        time.sleep(2)
        buscar(inp2)
        time.sleep(0.3)
        pyautogui.click(809, 422,clicks=2)
        pyautogui.typewrite(inp1)
        time.sleep(0.5)