num = int(input("Digite um numero"))
num1 = int(input("Digite outro numero"))
num2 = int(input("Digite mais um numero"))



if num > num1:
    if num > num2:
        print("O primeiro é maior")
if num1 > num:
    if num1 > num2:
        print("O segundo é maior")
if num2 > num:
    if num2 > num1:
        print("O terceiro é maior")