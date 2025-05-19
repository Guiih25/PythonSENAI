from datetime import datetime

nome = input("Digite seu nome: ")


def hora_atual():
    hora = datetime.now().hour
    return hora


def saudação():
    if hora_atual() >= 0 and hora_atual() <= 5:
        print("Boa madrugada", nome)

    elif hora_atual() > 5 and hora_atual() <= 12:
        print("Bom dia", nome, ", vamos acordar")

    elif hora_atual() > 12 and hora_atual() <= 19:
        print("Boa tarde", nome)

    elif hora_atual() > 19 and hora_atual() >= 23:
        print("Boa noite", nome)

saudação()
    


    