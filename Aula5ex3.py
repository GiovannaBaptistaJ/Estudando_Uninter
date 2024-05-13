def validar (pergunta, min, max):
    
    x = int(input(pergunta))
    while (x < min) or (x > max):
        x = x = int(input(pergunta))
    return x

def fatorial (num):
    """
    Função que calcula a fatorial de um número inteiro
    :param num:
    :return:
    """
    
    fat = 1
    if num == 0:
        return fat
    # Esta parte só executa caso num for maior que 0
    for i in range(1, num + 1, 1):
        fat = fat * i
    return fat

x = validar('Digite um valor para calcular o fatorial: ', 0, 9999999999)
print(f'{x}! = {fatorial(x)}')
help(fatorial)