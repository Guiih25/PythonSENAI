idade = int(input("Qual o ano em que você nasceu?"))
sub = 2025 - idade
calculo = ""

if sub >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")
print(sub, calculo)