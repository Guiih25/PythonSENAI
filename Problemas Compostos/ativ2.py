#adquirir o nome e o preço de um produto
#fazer o valor dividido por 20
#com o resultado você subtrai o valor pelo resultado da porcentagem
#exibir o valor
nome = input("Digite seu nome:")
print("Olá", nome, ",você ganhou um desconto de 5% em qualquer produto da loja!")


produto = input("Solicite o nome do produto:")
valor = float(input("Qual o valor do produto:"))
porcentagem = valor / 20
resultado = valor - porcentagem
print("O resultado do seu desconto é:", resultado, "Reais", "com o desconto de", porcentagem, "Reais")