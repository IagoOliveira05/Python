import pyautogui
import pyperclip

from datetime import datetime
from time import sleep

pyautogui.PAUSE = 4


def informacoes(contato, mensagem, horario=''):
    
    """
    -> Irá fazer a automação toda
    :param contato: nome do contato salvo em seu WPP (Obrigatório)
    :param mensagem: a mensagem que você deseja enviar (Obrigatório)
    :horario: o horário que você deseja enviar a mensagem. ex.: 12:35:10.  (Caso não seja dado ele enviará quando dar o OK)
    """
    hora = ''
    while True:
        if hora == horario:
            # --> Entrar no WPP
            pyautogui.alert("Aperte OK para começar o programa!")
            pyautogui.press("win")
            sleep(3)
            pyautogui.write("Chrome")
            pyautogui.press("enter")
            sleep(15)
            link= "https://web.whatsapp.com/"
            pyperclip.copy(link)
            pyautogui.hotkey("ctrl", "v")
            pyautogui.press("enter")

            # --> Entrar na mensagem do contato
            sleep(
                14
            )
            pyautogui.click(x=370, y=243)   # Barra para pesquisar o nome
            pyautogui.write(contato)       # Nome do contato
            pyautogui.press("enter")

            # --> Escrever e enviar mensagem
            msg = mensagem
            pyperclip.copy(msg)
            pyautogui.hotkey("ctrl", "v")
            pyautogui.press("enter")
            break
        else:
            atual = datetime.now()
            hora = atual.strftime('%H:%M:%S')


informacoes(contato="Duda", mensagem="Oi fedida")
