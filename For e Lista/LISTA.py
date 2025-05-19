#lista com 5 objetos
quarto = ['Cadeira', 'Cama', 'Estante', 'Comoda', 'Guarda-Roupa']
print("Lista de objetos criadas")
print(quarto)

#adicionei mais um item ao final da lista
quarto.append('Travesseiro')
print('Travesseiro adicionado')
print(quarto)


#exibir o 2°
print('Segundo objeto', quarto[1])


#remover um objeto e exibilo
quarto.remove("Estante")
print('A estante foi removida')
print(quarto)


#exibir o tamanho da lista
print("Total de objetos")
print(len(quarto))

#mostre os itens com o for
print("LISTA")

for x in quarto:
    print(x)
print("")

#verificar itens na lista
if 'Cadeira' in quarto:
    quarto.remove('Cadeira')
    print('Cadeira removida')
    print(quarto)
else:
    quarto.append('Cadeira')
    print(quarto)

#ordenar a lista
print("Antes")
print(quarto)
quarto1 = quarto.sort()
print("Depois")
print('Lista ordenada')
print(quarto)
#exibir o numero da lista
print("Total de objetos")
print(len(quarto))
print("Primeiro objeto")
print(quarto[0])
print("Ultimo objeto")
print(quarto[-1])
#limpar toda a lista
print("Lista limpa")
quarto.clear()