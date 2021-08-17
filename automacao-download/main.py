# link = https://www.youtube.com/watch?v=xAM51Ovpr9M

from selenium import webdriver
import pyautogui
from time import sleep


link = str(input("Link dad música que deseja baixar: "))

navegador = webdriver.Chrome()
navegador.get('https://www.snappea.com/pt1/')

navegador.find_element_by_xpath('//*[@id="searchContent"]').send_keys(link)
sleep(2)
pyautogui.press("enter")
sleep(7)
navegador.find_element_by_xpath('//*[@id="downloadBtn"]').click()
sleep(15)
navegador.quit()