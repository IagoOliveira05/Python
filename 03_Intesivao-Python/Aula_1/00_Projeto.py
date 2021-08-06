# Bibliotecas
import pyautogui
import pyperclip
import time
import pandas as pd


# Passo 1: Entrar no sistema (Link do Google Drive = https://onedrive.live.com/?authkey=%21ALJ4pCaq3Iy2pUI&id=29B93B5F81DEAF2F%21199766&cid=29B93B5F81DEAF2F)

#pyautogui.alert("Aperte OK para o programa possa iniciar!")

pyautogui.PAUSE = 4
pyautogui.press('win')  
time.sleep(1)
pyautogui.write('chrome')
time.sleep(1)
pyautogui.click(x=209, y=292)
link_pasta = "https://onedrive.live.com/?authkey=%21ALJ4pCaq3Iy2pUI&id=29B93B5F81DEAF2F%21199766&cid=29B93B5F81DEAF2F"
pyperclip.copy(link_pasta)
time.sleep(2)
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')

# Passo 2: Entrar na pasta da Aula 1https://onedrive.live.com/?authkey=%21ALJ4pCaq3Iy2pUI&id=29B93B5F81DEAF2F%21199766&cid=29B93B5F81DEAF2F


time.sleep(10)
pyautogui.click(x=434, y=441)

# Passo 3: Fazer o download da Base de Vendas

pyautogui.click(x=1214, y=378)
pyautogui.click(x=568, y=208)

# Passo 4: Calcular os indicadores (Faturamento e a Quantidade de Produtos)

arquivo = pd.read_excel(r"C:\Users\Iago\Downloads\Vendas.xlsx")
faturamento = arquivo["Valor Final"].sum()
quant_produtos = arquivo["Quantidade"].sum()

# Passo 5: Entrar no meu email

pyautogui.hotkey('ctrl', 't')
link_email = "https://outlook.live.com/mail/0/inbox"
pyperclip.copy(link_email)
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')

# Passo 6: Criar o email

time.sleep(12)
pyautogui.click(x=193, y=203)
time.sleep(8)
email = "iago2011.andrade+diretoria@hotmail.com"
pyperclip.copy(email)
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
assunto = 'Relatório de Vendas'
pyperclip.copy(assunto)
pyautogui.hotkey('ctrl', 'v')
time.sleep(1)
pyautogui.press('tab')
msg = f"""
Prezados, boa noite

O faturamento foi de R${faturamento:,.2f}
A quantidade de produtos foi de: {quant_produtos:,}

Abs
Iago Oliveira
"""
pyperclip.copy(msg)
pyautogui.hotkey('ctrl', 'v')

# Passo 7: Enviar o email (iago2011.andrade+diretoria@hotmail.com)
time.sleep(2)
pyautogui.hotkey('ctrl', 'enter')

#pyautogui.alert("Programa encerrado com sucesso!")