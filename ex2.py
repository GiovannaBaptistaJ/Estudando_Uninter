va = int(input('Quantos km percorridos do carro alugado?'))

dia = int(input('Por quantos dias foram percorridos?'))

caldia = dia * 60

calkm = va * 0.15

valor = caldia + calkm

resultado = f'O preço a se pagar será de R$ {valor}'

print(resultado)