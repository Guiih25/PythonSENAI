import inputs

def verificar_numeros(numero):
    
    if num >= 0:
        print("Seu numero é positivo")
        return True
        
    else:
        print("Seu numero é negativo")
        return False
num = inputs.input_int("Digite o numero: ")
verificar_numeros(num)