from tkinter import *
from selenium import webdriver

class Tela():
    def __init__(self):
        self.root = root
        self.configura_tela()
        self.widgets()
        root.mainloop()

    def configura_tela(self):
        self.root.title("Search Bar")

    def widgets(self):
        text_URL = Label(
            self.root,
            text="Coloque a URL aqui:",
            font=("arial",10,"bold")
        )
        text_URL.grid(row=0, column=0)

        entrada = Entry(
            self.root,
            width=30
        )
        entrada.grid(row=0, column=1)

        self.btn_procura = Button(
            self.root,
            text="Procurar",
            command=self.procurar
        )
        self.btn_procura.grid(row=1, column=0, columnspan=2, pady=10)

    def procurar(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.youtube.com/watch?v=xAM51Ovpr9M')

root = Tk()
Tela()