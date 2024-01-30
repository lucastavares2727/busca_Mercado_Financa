import yfinance
import pyautogui
import time
import pyperclip
import pyscreeze
from PIL import Image
cod=input("Digite o codigo da acao :")
time.sleep(5)
f=yfinance.Ticker(cod).history("6Mo")
fechamento=f.Close#fechamento
maximo=fechamento.max()#maximo fechamento
minimo=fechamento.min()##valor minimo
atual=fechamento[-1]
time.sleep(2)
pyautogui.hotkey("alt", "tab")
time.sleep(2)
pyperclip.copy("www.gmail.com")
time.sleep(2)
pyautogui.hotkey("ctrl","v")
time.sleep(2)
pyautogui.hotkey("enter")
time.sleep(2)
pyautogui.click(x=46, y=226) #ATALHO DO " ESCREVER"
pyperclip.copy("lucas.a.tavares27@gmail.com")
time.sleep(2)
pyautogui.hotkey("ctrl","v")
time.sleep(2)
pyautogui.hotkey("tab")
time.sleep(2)
pyperclip.copy("Analise de valores")
time.sleep(2)
pyautogui.hotkey("ctrl","v")
time.sleep(2)
pyautogui.hotkey("tab")

msg=f"""

SEGUE RE LATORIO DOS ULTIMOS 6 MESES DA ACAO = {cod}
Cotacao maxima = {maximo}
Cotacao minima = {minimo}
Cotacao atual  = {atual}
"""
pyperclip.copy(msg)
time.sleep(2)
pyautogui.hotkey("ctrl","v")


pyautogui.click(x=1300, y=1004)#BOTAO ENVIAR
