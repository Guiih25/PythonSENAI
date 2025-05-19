def menu_calculadora():
    print("Menu:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Divisão")
    print("4 - Multiplicação")
    print("5 - Todas as opções")

def soma(num1, num2):
    return num1 + num2

def subtração(num1, num2):
    return num1 - num2

def divisão(num1, num2):
    return num1 / num2

def multiplicação(num1, num2):
    return num1 * num2

def Conta_escolhida():
    if conta == 1:
        print("O resultado da soma é", soma(num1, num2))

    elif conta == 2:
        print("O resultado da subtração é", subtração(num1, num2))

    elif conta == 3:
        print("O resultado da divisão é", divisão(num1, num2))

    elif conta == 4:
        print("O resultado da multiplicação é", multiplicação(num1, num2))

    elif conta == 5:
        print("O resultado da soma é", soma(num1, num2))
        print("O resultado da subtração é", subtração(num1, num2))
        print("O resultado da divisão é", divisão(num1, num2))
        print("O resultado da multiplicação é", multiplicação(num1, num2))

           
while True:            
    try:
        num1 = int(input("Escolha um número: "))
        break
    except ValueError:
        print("Digite somente números. Exp:(37)")
   
while True:
    try:
        num2 = int(input("Escolha outro número: "))
        break
    except ValueError:
        print("Digite somente números. Exp:(12)")
   
menu_calculadora()
conta = int(input("Escolha uma opção: "))

Conta_escolhida()