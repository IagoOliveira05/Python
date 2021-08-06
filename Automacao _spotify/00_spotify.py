import pyautogui
import pyperclip
import time

# BOTÃO "Play": x=894, y=367

pyautogui.PAUSE = 7

pyautogui.press("win")
pyautogui.write("Spotify")
pyautogui.press("enter")
time.sleep(13)
pyautogui.hotkey("ctrl", "l")
pyautogui.write("Iago")
pyautogui.click(x=894, y=367)
