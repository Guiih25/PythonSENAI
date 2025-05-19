nota = int(input("Insira sua nota: "))
nota2 = int(input("Insira sua outra nota: "))

soma = nota + nota2
divisao = soma / 2
if nota > 0 and nota <= 100 and nota2 >= 0 and nota2 <= 100:

    if divisao >= 70:
        print("Aprovado")
    elif divisao >= 50 and divisao < 70:
        print("Recuperação")
    elif divisao < 50:
        print("Reprovado")
        
    print("Sua nota foi:", divisao)
else:
    print("De 0 a 100")
