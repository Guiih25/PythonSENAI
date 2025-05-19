#1 - Adquirir um valor de salario

#2 - VAlor do salario com 10% de aplicaçao

#3
#pego o salario e divido pela porcentagem
#pego o resultado e somo com o salario
#exibir o resultado


nome = input("Digite seu nome: ")
print("Ola", nome)


salario = float(input("Solicite o seu salario aqui:"))
divisão = salario / 10
soma = divisão + salario

print(nome, "O valor do seu salario com acrescimo de 10% é:", soma )


print("Seu salario é", soma, "com acrescimo de", divisão)

print("Parabens", nome)
