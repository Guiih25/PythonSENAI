import inputs
print("Sistema de gerenciamento  de inscrições")
nomes = []

while True:
    
    print("MENU")
    print('[1] - Cadastrar nomes')
    print('[2] - Exibir total de inscritos')
    print('[3] - exibir a lista em ordem alfabetica')
    print('[4] - Consulta de nome')
    print("[0] - Sair")
    
    menu = inputs.input_int("Digite sua opçõa aqui: ")
    if menu == 0:
        break
    
    elif menu == 1:
        print("Vamos cadastar seu nome: ")
        nome = inputs.input_str("Digite o nome desejado: ")
        if nome in nomes:
            print("Seu nome já esta na lista")
            print(nomes)
            continuar = inputs.input_str("Deseja continuar? (s/n)")
            if continuar == "n":
                print("Fim")
                break
            else:
                continue   
        else:
            nomes.append(nome)
            print("Nome adicionado")
            print(nomes)
            continuar = inputs.input_str("Deseja continuar? (s/n)")
            if continuar == "n":
                break
            else:
                continue
            
    elif menu == 2:
        print("Quantidade de Inscritos")
        print(len(nomes))
        continuar = inputs.input_str("Deseja continuar? (s/n)")
        if continuar == "n":
            print("Fim")
            break
        else:
            continue
    elif menu == 3:
        nomes.sort()
        for x in nomes:
            print(x)
        continuar = inputs.input_str("Deseja continuar? (s/n)")
        if continuar == "n":
            print("Fim")
            break
        else:
            continue
    
    elif menu == 4:
        nomex = inputs.input_str("Digite o nome desejado: ")
        if nomex in nomes:
            print("Nome encontrado")
            remover = inputs.input_str("Deseja removelo?(s/n): ")
            if remover == "s":
                print("Nome removido")
                nomes.remove(nomex)
                print(nomes)
                continuar = inputs.input_str("Deseja continuar? (s/n)")
                if continuar == "n":
                    print("Fim")
                    break
                else:
                    continue
            else:
                print("Nome não removido")
                print(nomes)
                continuar = inputs.input_str("Deseja continuar? (s/n)")
                if continuar == "n":
                    print("Fim")
                    break
                else:
                    continue
                
                if continuar == "n":
                    print("Fim")
                    break
                else:
                    continue
        else:
            print("Nome não encontrado")
            desejo = inputs.input_str("Deseja adicionalo? (s/n)")
            if desejo == 's':
                print("Nome adicionado")
                nomes.append(nomex)
                print(nomes)
                continuar = inputs.input_str("Deseja continuar? (s/n)")
                if continuar == "n":
                    print("Fim")
                    break
                else:
                    continue
            else:
                print("Nome não adicionado")
                continuar = inputs.input_str("Deseja continuar? (s/n)")
                if continuar == "n":
                    print("Fim")
                    break