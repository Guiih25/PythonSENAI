def menu():
    print("Escolha sua operação desejada: ")
    print("1   -   Soma")
    print("2   -   Subtração")
    print("3   -   Multiplicação")
    print("4   -   Divisão")
    escolha = input("Digite aqui: ")
    

    if escolha == "1":
        print("O resultado da sua soma é", soma1())
        
    elif escolha == "2":
        print( "O resultado da sua subtração foi", subtracao())
        
    elif escolha == "3":
        print("Sua multiplicação foi", multiplicacao())
        
    elif escolha == "4":
        print("O resultado foi", divisao())
    
     
 
def soma1():
    soma = num1 + num2
    return soma

def subtracao():
    sub = num1 - num2
    return sub

def multiplicacao():
    mult = num1 * num2
    return mult


def divisao():
    divi = num1 / num2
    return divi



num1 = int(input("Digite um numero: "))
num2 = int(input("Digite outro numero: "))

menu()
