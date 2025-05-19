def calcula_imc(peso, altura):   
    imc1 = peso / (altura * altura)
    return imc1

def resultado():
    print("Seu IMC é:", round(calcula_imc(peso, altura), 3))


def tabela_imc(imc):
    resultado()
    if calcula_imc(peso, altura) <= 18.5:
        print("Magreza")
    
    elif calcula_imc(peso, altura) > 18.5 and calcula_imc(peso, altura) <= 24.9:
        print("Normal")
    
    elif calcula_imc(peso, altura) > 24.9 and calcula_imc(peso, altura) <= 29.9:
        print("Sobrepeso")
        
    elif calcula_imc(peso, altura) > 29.9 and calcula_imc(peso, altura) <= 34.9:
        print("Obesidade 1°")
    
    elif calcula_imc(peso, altura) > 34.9 and calcula_imc(peso, altura) <= 39.9:
        print("Obesidade 2°")
    
    elif calcula_imc(peso, altura) > 39.9:
        print("Obesidade 3°")


peso = int(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
imc = calcula_imc(peso, altura)

tabela_imc(imc)
