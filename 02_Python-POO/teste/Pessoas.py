
class Pessoa:
    def __init__(self, nome, idade, comendo=False, falando=False, andando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando
        self.andando = andando

    def comer(self, alimento):
        if self.comendo:
            print(f"{self.nome} já está comendo")
            return
        
        if self.falando:
            print("Não pode comer enquanto fala!")
            return

        print(f"{self.nome} está comendo {alimento}.")
        self.comendo = True

    def parar_comer(self):
        if not self.comendo:
            print(f"{self.nome} não está comendo!")
            return

        print(f"{self.nome} parou de comer.")
        self.comendo = False

    def falar(self, assunto):
        if self.falando:
            print(f"{self.nome} já está falando.")
            return

        if self.comendo:
            print("Não pode falar enquanto come!")
            return

        print(f"{self.nome} está falando sobre {assunto}.")
        self.falando = True

    def parar_falar(self):
        if not self.falando:
            print(f"{self.nome} não está falando!")
            return
        
        print(f"{self.nome} parou de falar.")
        self.falando = False

    def andar(self, direcao):
        if self.andando:
            print(f"{self.nome} já está andando!")
            return

        print(f"{self.nome} está andando para a {direcao}.")
        self.andando = True

    def parar_andar(self):
        if not self.andando:
            print(f"{self.nome} não está andando!")
            return
        
        print(f"{self.nome} parou de andar.")
        self.andando = False