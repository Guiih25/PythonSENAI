
def calcular_fairi(temperatura):
    return temperatura * 1.8 + 32

    
    
def calcular_kalvin(temperatura):
    return temperatura + 273


temperatura = float(input("Digite sua temperatura: "))

print(temperatura, "°C")
print(calcular_fairi(temperatura), "°F")
print(calcular_kalvin(temperatura), "K")
