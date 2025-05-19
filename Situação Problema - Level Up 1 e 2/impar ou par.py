import random

n_ale = random.randint(1,10)
while True:
    print("MENU")
    
    print("Escolha Impar ou Par")
    print("[1] - Impar")
    print("[2] - Par")
    print("[3] - Parar")

    jogo = int(input("Escolha uma opção: "))

    if jogo == 1:
        num = print("Você escolheu impar")
        print("Seu oponete escolheu par")
        num1 = int(input("Escolha um numero para começar o jogo(1 a 10): "))
        soma = num1 + n_ale
        if soma % 2 == 0:
            print("Seu jogo deu Par")
            
            print("Seu oponente escolheu", n_ale)
            print("O resultado foi", soma)
            print("VOCÊ PERDEU!")
        else:
            print("Seu jogo deu Impar")

            print("Seu oponente escolheu", n_ale)
            print("O resultado foi", soma)
            print("VOCÊ GANHOU!!!!", soma)

    elif jogo == 2:
        num = print("Você escolheu Par")
        print("Seu oponete escolheu Impar")
        num1 = int(input("Escolha um numero para começar o jogo(1 a 10): "))
        soma = num1 + n_ale
        if soma % 2 == 0:
            print("Seu jogo deu Par")
            
            print("Seu oponente escolheu", n_ale)
            print("O resultado foi", soma)
            print("VOCÊ GANHOU!!!")
        else:
            print("Seu jogo deu Impar")
            print("VOCÊ PERDEU!!!", soma)
    elif jogo == 3:
        print("Volte mais tarde ^_^")
        break
    

        
    