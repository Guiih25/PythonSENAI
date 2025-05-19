#1 quantos litros e qual valor que serao necessarios para completar a viagem
# qual a distancia da viagem
# quantos km ja foram percorridos
# qual a autonomia do carro por litro
# quantos litros ha no tanque
# qual o preço do combustivel

#2 passo a passo
#subtarir a distancia por quanto foi percorrido
# dividir a distancia pela autonomia
# subtrair o combustivel pelo litro
# multiplicar o valor pelo preço
# exibir o valor gasto em reais e o quanto de combustivel sera necessario


viagem = 800
autonomia = 7
tanque = 10
distancia = 90
preco = 6.90

Km = int(viagem - distancia)
litro1 = int(Km / autonomia)
litro2 = int(litro1 - tanque)
valor1 = int(litro2 * preco)
print("O valor do combustivel foi de: R$", (valor1))
print("Serão necessarios", litro2, "Litros")