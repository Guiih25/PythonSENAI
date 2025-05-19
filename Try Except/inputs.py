def input_int(mensagem):
    while True:
        try:
            num1 = int(input(mensagem))
            print(num1)
            return num1
        except ValueError:
            print("Digite somente números. Exp:(37)")
        
def input_float(numeros):
     while True:
         try:
             num = float(input(numeros))
             print(num)
             return num
         except ValueError:
            print("Digite somente números. Exp:(3,7)")

def input_str(letra):
    while True:
        pala = str(input(letra))
        print(pala)
        if not pala.isalpha():
            print("Digite somente letras")
        else:
            return pala