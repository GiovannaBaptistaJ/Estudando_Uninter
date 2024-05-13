pre = int(input ('Digite o preço do produto'))
perc = int(input ('Digite o desconto'))

calculo = perc / 100 * pre

resultado = pre - calculo

resposta = f'O valor do desconto foi {calculo} e o preço final do produto é {resultado}'

print(resposta)

