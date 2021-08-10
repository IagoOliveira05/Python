from Pessoas import Pessoa

nome = str(input("Seu nome: "))
idade = int(input("Sua idade: "))
p1 = Pessoa(nome, idade)


p1.andar('direita')
p1.parar_andar()