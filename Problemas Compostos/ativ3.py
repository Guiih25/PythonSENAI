#1 - Saber o valor que falta para completar o tanque

#2 - informações
#capacidade do carro
#subtrair a capacidade pelo combustivel atual
#multiplicar o valor que falta para completar o tanque pelo preço
#exibir

tanque = int(input("Digite a capacidade do tanque:"))
carro = int(input("Digite quantos litros tem no tanque:"))
preco = float(input("Digite o valor do litro:"))

subtracao = tanque - carro
multiplicacao = subtracao * preco
print("O valor ultilizado para encher o tanque é: R$", multiplicacao)