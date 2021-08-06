import pyautogui

from time import sleep
import random

pyautogui.PAUSE = 3
pyautogui.confirm("Pressione OK para começar")
sleep(2)
tempo = random.randint(8, 17)  #Escolhe um número entre 8seg e 17seg
pyautogui.confirm(f'{"Vá para o Kwai!".center(35)}\nCaso já esteja pressione "OK"')

while True:
    sleep(tempo)   # Esperar o vídeo acabar
    pyautogui.scroll(-100)  # Rolar para baixo
