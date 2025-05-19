gran  = 0
quant = 0

while True:
    print("MENU")
    print("")
    print("[1] Adicionar o valor da despesa")
    print("[2] mostrar quantidade e valor total das despesas")
    print("[0] sair")
    num = input("Selecione uma das opições: ")


    if num == "1":
        gasto = int(input("valor gasto: "))
        print(gasto, "reais")
        gran = gran + gasto
        quant += 1
    elif num == "2":
        print("O valor gasto foi de:", gran ,'reais')
        print('quantidade de despesas:',quant)
    elif num == "0":
        print("BYEEEE BYEEE")
        break