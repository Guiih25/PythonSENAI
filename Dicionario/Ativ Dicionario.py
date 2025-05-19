Apple = {
    'Marca': 'Apple',
    'Modelo': 'Iphone 15 Pro',
    'Preço': 7.100,
    'Armazenamento': '128Gb-1TB: Ram:8gb'  
}
Samsung = {
    'Marca': 'Samsung',
    'Modelo': 'S25 Ultra',
    'Preço': 8.000,
    'Armazenamento': '128Gb-512: Ram:12gb'   
}
Xiaomi = {
    'Marca': 'Xiaomi',
    'Modelo': 'Xiaomi 15 Ultra',
    'Preço': 11.000,
    'Armazenamento': '128Gb-1TB: Ram:8-16gb'   
}

#exibir uma lista de dicionarios
lista_marca = [Apple, Samsung, Xiaomi]

     #escolhendo os campos


     #exibindo todos
for marca in lista_marca:
    for chave, valor in marca.items():
        print(f' {chave}:  {valor}')
    print("")