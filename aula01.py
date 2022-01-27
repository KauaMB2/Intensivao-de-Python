from IPython.display import display
import pyautogui as pg
import pyperclip as pc
import time
import os
import pandas as pd
pg.PAUSE=1
pg.hotkey("ctrl","t")
time.sleep(7)
link1="https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga"
pc.copy(link1)
pg.hotkey("ctrl","v")
pg.press("enter")
time.sleep(17)
pg.click(x=345,y=268,clicks=2)
time.sleep(5)
pg.click(x=345,y=268)
pg.click(x=815, y=152)
pg.click(x=528, y=557)
link2="https://mail.google.com/mail/u/0/#inbox"
pc.copy(link2)
pg.hotkey("ctrl","t")
time.sleep(5)
pg.hotkey("ctrl","v")
pg.press("enter")
time.sleep(12)
pg.click(x=42,y=156)
time.sleep(25)
email="i.kauamoreirabatista@gmail.com"
pc.copy(email)
pg.hotkey("ctrl","v")
pg.press("tab")
assunto="Relatório de vendas"
tabela=pd.read_excel(r"C:\Users\Rafael\Downloads\Vendas - Dez.xlsx")
faturamento=tabela["Valor Final"].sum()
qntdProduto=tabela["Quantidade"].sum()
pc.copy(assunto)
pg.hotkey("ctrl","v")
pg.press("tab")
texto=f"""
Olá, bom dia!
O faturamento de ontem foi de: {faturamento}
A quantidade de produtos foi de {qntdProduto}
Abs, Kauã.
"""
pc.copy(texto)
pg.hotkey("ctrl","v")
pg.hotkey("ctrl","enter")