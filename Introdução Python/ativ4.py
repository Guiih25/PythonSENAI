# Solicita o número para o usuário
numero = int(input("Digite um número para ver sua tabuada: "))

# Imprime a tabuada
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")