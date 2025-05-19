ano = int(input("Digite seu ano de nascimento: "))
nasci = 2025 - ano 

if nasci >= 60:
    print("Idoso")


elif nasci >= 18 and nasci <= 59:
    print("Adulto")


elif nasci >= 11 and nasci <= 17:
    print("Adolecente")


elif nasci <= 10:
    print("Criança")


print("Sua idade é:", nasci)