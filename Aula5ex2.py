def validar(pergunta, min, max):
    s1 = input(pergunta)
    tam = len(s1)

    while (tam < min) or (tam > max):
        s1 = input(pergunta)
        tam = len(s1)
    return s1

x = validar('Digite uma string:', 10, 30)

print(f'Você digitou a string: {x}. \n Dado válido. Encerrando o programa...')
