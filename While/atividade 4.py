while True:
    print('*MENU DE OPERAÇÕES*')
    print('')
    print("[1] - Fatorial")
    print("[2] - Quadrado")
    print("[3] - Cubo")
    print("[4] - Tabuada")
    print("[0] - Sair")
    num = int(input("Selecione a opção desejada: "))
    
    if num == 1:
        num1 = int(input("Digite o numero que deseja fatoriar"))
        fatorial = 1
        while num1 > 0:
            fatorial = fatorial * num1
            num1 = num1 - 1
        print("A fatorial do numero solicitado é:", fatorial)
            
    elif num == 2:
        num1 = int(input("Digite o numero que deseja ver o quadrado: "))
        nume = num1 * num1
        print("O Quadrado do seu numero é:", nume)
        
        
    elif num == 3:
        num1 = int(input("Digite o numero que deseja ver o cubo: "))
        numex = num1 * num1 * num1
        print("O cubo do seu numero é:", numex)
        
        
    elif num == 4:
        num = int(input("Digite um numero para ver a tabuada: "))
        resultado = num * 1
        print(num, "x 1 = ", resultado)

        resultado = num * 2
        print(num, "x 2 = ", resultado)

        resultado = num * 3
        print(num, "x 3 = ", resultado)

        resultado = num * 4
        print(num, "x 4 = ", resultado)

        resultado = num * 5
        print(num, "x 5 = ", resultado)

        resultado = num * 6
        print(num, "x 6 = ", resultado)

        resultado = num * 7
        print(num, "x 7 = ", resultado)

        resultado = num * 8
        print(num, "x 8 = ", resultado)

        resultado = num * 9
        print(num, "x 9 = ", resultado)

        resultado = num * 10
        print(num, "x 10 = ", resultado)
        
    elif num == 0:
        print("Bye, volte mais tarde :D")
        break
        
        
        