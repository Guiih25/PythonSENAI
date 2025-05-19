n = int(input("Numero: "))

num = 0

quant = 0


while True:
    num = num + 1
    if num % 2 == 0:
        print(num)
        # somando a quantidade de pares
        quant = quant + 1
       
        
   
    if num > n:
        break
print("")
print("A quantidade de pares é:", quant)


        