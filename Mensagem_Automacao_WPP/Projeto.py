import pywhatkit as pwk

print("Preencha os campos abaixos")
numero_telefone = str(input("Número de telefone (com DDD): +55")).strip()
hora = int(input("Hora que deseja enviar: "))
minuto = int(input("Minuto que deseja enviar: "))
mensagem = str(input("Mensagem que deseja enviar: "))

pwk.sendwhatmsg(f"+55{numero_telefone}", mensagem, hora, minuto)
