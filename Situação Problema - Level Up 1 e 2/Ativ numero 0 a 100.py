import random

pc = random.randint(0,100)
def menu():
    print("Vamos jogar!")
    print("Adivinhe um numero (0 a 100)")
    print("[1] - CONTINUAR")
    print("[2] - SAIR")
    
menu()
nume = int(input("Digite a opção aq: "))

if nume == 1:
    print("VAMOS COMEÇAR")
    while True:
        
        num = int(input("Digite seu numero aqui: "))
        if num == pc:
            print("Seu numero esta correto!!!!!!!!!!", "ele é", pc)
            menu()
            pc = random.randint(0,100)
            nume = int(input("Dgite a opção aq: "))
            if nume == 2:
                print("Volte mais tarde!")
                break
            
                
        elif pc > num:
            print("Seu numero é maior que", num)
        
        elif pc < num:
            print("Seu numero é menor que", num)
elif nume == 2:
    print("Volte mais tarde")