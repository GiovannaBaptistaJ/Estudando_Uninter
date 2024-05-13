print ('Fruteira Preço Bom!')

valor = 0

while (valor != 1 and valor != 2 and valor != 3):
  valor = int(input('Digite o número da fruta, 1 para maçã, 2 para laranja e 3 para banana:  '))

if (valor == 1):
        print('Você escolheu maçã! O valor para cada maçã é 2,30.')
        dec = int(input('Quantas desejas comprar? '))
        precototal = dec * 2.30
        print (f'O valor total foi de: {precototal}')
elif (valor == 2):
        print('Você comprou laranja')
        dec = int(input('Quantas desejas comprar? '))
        precototal = dec * 3.60
        print (f'O valor total foi de: {precototal}')
elif (valor == 3):
        print('Você comprou banana')
        dec = int(input('Quantas desejas comprar? '))
        precototal = dec * 1.85
        print (f'O valor total foi de: {precototal}')
else:
       print('FRUTA NÃO ENCONTRADA')
