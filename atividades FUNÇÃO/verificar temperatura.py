import inputs
estacao = inputs.input_str("Digite V/I: ")
temperatura = inputs.input_int("Digite a temperatura: ") #variaves presentes na função
humidade = inputs.input_int("Digite a humidade: ")


def cadastrar_temperatura(estacao, temperatura, humidade):  #função com os parametros selecionados
    if estacao == "V":
        if temperatura >= 23 and temperatura <= 26:
            if humidade >= 40 and humidade <= 65:
                print("A Qualidade do ar esta ideal")
            else:
                print("A qualidade não esta ideal")
        else:
            print("A qualidade não esta ideal")
    elif estacao == "I":
        if temperatura > 20 and temperatura < 22:
            if humidade > 40 and humidade < 55:
                print("A qualidade do ar está ideal")
            else:
                print("A qualidade não esta ideal")
        else:
            print("A qualidade não eta ideal")
            
cadastrar_temperatura(estacao, temperatura, humidade) #chamei a função
