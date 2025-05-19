print("Vamos calcular seu IMC!")

peso = int(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc2 = altura * altura
imc = peso / imc2

if imc <= 18.5:
    print("Magreza")

elif imc >= 18.6 and imc <= 24.9:
    print("Normal")
elif imc >= 25 and imc <= 29.9:
    print("Sobrepeso")

elif imc >= 30 and imc <= 34.9:
    print("Obesidade 1°")
elif imc >= 35 and imc <= 39.9:
    print("Obesidade 2°")
elif imc >= 40:
    print("Obesidade 3°")
print(imc)
