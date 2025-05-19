import inputs
while True:
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

               
               
     
    num1 = inputs.input_int("Escolha um número: ")
        
    num2 = inputs.input_int("Escolha outro número: ")
 
       
    menu_calculadora()
    conta = inputs.input_int("Escolha uma opção: ")
    Conta_escolhida()
    continuar = input("Deseja continuar? (s/n): ")
    
    
    
    if continuar == "n":
        print("Fim")
        break
    else:
        continue   