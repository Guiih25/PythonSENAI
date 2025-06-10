import inputs #importa o imputs

alunos = [] # lista para guardar o dicionario

def calcular_media(nota1, nota2, nota3): #ele calcula as 3 notas e faz a média
    return (nota1 + nota2 + nota3) / 3

def cadastrar_aluno(): #aqui é onde o aluno se cadastra com nome e  as 3 notas
    nome = inputs.input_str("Digite o nome do aluno: ")
    nota1 = inputs.input_int("Digite a primeira nota: ")
    nota2 = inputs.input_int("A segunda nota: ")
    nota3 = inputs.input_int("E a terceira nota: ")
    media = calcular_media(nota1, nota2, nota3) #chamei a media que fiz em outra função
    situacao = verificar_situacao(media) # e chamei outra função que faz a situação do aluno
    aluno = {
        "nome": nome,
        "nota1": nota1,
        "nota2": nota2,
        "nota3": nota3,
        "media": media,                 #dicionario
        "situacao": situacao
    }
    print("")
    print("ALUNO CADASTRADO COM SUCESSO")
    print("")
    return aluno # ele retorna o aluno para eu chamar em outra função
    
def verificar_situacao(media): #verifica a situação do aluno
    if media >= 7:
        return "Aprovado"        #se o aluno tiver uma nota maior ou igual a 7 ele esta aprovado
    elif media >= 5 and media < 7:
        return "Recuperação" # se tirar entre 5 e 6,9 ele esta de recuperação
    else:
        return "Reprovado"  #menos que 5 reprovado

def mostrar_relatorio():  #relatorio do aluno com o nome, media e situação
    print("")
    print("----RELATÓRIO----")
    for aluno in alunos:
        print("--------------------------")
        print(f"Nome:  {aluno['nome']}")
        print(f"Media:  {aluno['media']}")
        print(f"Situação:  {aluno['situacao']}")
        print("-------------------------------")
        outra_opcao = inputs.input_str("Você deseja ver completo? (s/n)")
        if outra_opcao == "s":
            print("")
            print("----RELATÓRIO COMPLETO----")
            print("-----------------------")
            print(f"Nome:  {aluno['nome']}")
            print(f"Nota 1:  {aluno['nota1']}")
            print(f"Nota 2:  {aluno['nota2']}")
            print(f"Nota 3:  {aluno['nota3']}")
            print(f"Media:  {aluno['media']}")
            print(f"Situação:  {aluno['situacao']}")
            print("------------------------------")
        
            
        
def main():  #função para executar o codigo adicionando na lista para poder chamar ele no relatorio
    while True:
        alunos.append(cadastrar_aluno())
        
        coninuar = inputs.input_str("Deseja continuar com outro aluno? (s/n): ").lower()
        if coninuar != "s":
            break
        
while 1:
    
    print("")
    print("    --------MENU--------")
    print("")
    print("[1] - Cadastrar dados do aluno")
    print("------------------------------")
    print("[2] - Exibir relatorio")
    print("------------------------------")
    print("[0] - Sair")
    print("------------------------------")
    menu = inputs.input_int("Escolha a Opção desejada: ")
    if menu == 1:
        print("")
        main()
    elif menu == 2:
        print("")
        mostrar_relatorio()
    elif menu == 0:
        print("")
        print("Fim do programa!")
        print("")
        print("   ° ͜ʖ ͡°")
        break
    else:
        print("")
        print("Opção inexistente")
        