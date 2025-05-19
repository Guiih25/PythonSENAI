nota = int(input("digite sua primeira nota"))
nota2 = int(input("digite sua segunda nota"))


soma = nota + nota2
media = soma / 2

variavel = ""

if media >= 70:
    variavel = "Aprovado"
elif media < 70:
    variavel = "Reprovado"
print("Sua nota é:", media, "você foi", variavel)