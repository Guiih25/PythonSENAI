import inputs

distancia = inputs.input_int("Digite a distancia: ")
velocidade = inputs.input_int("Digite a velocidade: ")

def calcular_tempo(temp, velo):
    divisao = distancia/velocidade
    if divisao >= 1:
        print(f"Seu trajeto demorará {divisao} horas")
        
    else:
        num = 60 * divisao
        print(f"Seu trajeto vai demorar {num} Minutos para a chegada")
calcular_tempo(distancia, velocidade)