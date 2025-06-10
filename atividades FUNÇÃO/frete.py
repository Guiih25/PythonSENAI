import inputs
peso = inputs.input_float("Digite o peso do produto: ")
distancia = inputs.input_float("Digite a distancia: ")

taxa_fixa = 5.58

def calcular_valor_frete(p, d, t):
    peso1 = peso * 0.5
    dist = distancia * 0.1
    valor = peso1 + dist + taxa_fixa
    print(f"O valor do seu frete ficou {valor} reais")


calcular_valor_frete(peso, distancia, taxa_fixa)