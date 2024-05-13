print('Lanchonete!')
print('1 - Coxinha - R$ 5,00')
print('2 - Pastel - R$ 7,00')
print('3 - Café - R$ 4,00')
print('4 - Suco - R$ 6,00')

total = 0
coxinha = 0
pastel = 0
cafe = 0
suco = 0

R = input('Desejas comprar algo? S/N:   ') 

while ( R == 'S'):
    i = int(input('Qual item desejas comprar? '))
    if (i == 1):
            quant = int(input('Qual a quantidade? '))
            total = quant * 5.00
            print (f'Você escolheu coxinha e comprou {quant} unidades. Pagará R$ {total} por elas')
            coxinha = coxinha + total
            R = input('Deseja continuar? ')
    elif (i == 2):
            quant = int(input('Qual a quantidade ?'))
            total = quant * 7.00
            print (f'Você escolheu pastel e comprou {quant} unidades. Pagará R$ {total}')
            pastel = pastel + total
            R = input('Deseja continuar? ')  
    elif (i == 3):
            quant = int(input('Qual a quantidade? '))
            total = quant * 4.00
            print (f'Você escolheu café e comprou {quant} unidades. Pagará R$ {total}')
            cafe = cafe + total
            R = input('Deseja continuar ?')  
    elif (i == 4):
            quant = int(input('Qual a quantidade?'))
            total = quant * 6.00
            print (f'Você escolheu suco e comprou {quant} unidades. Pagará R$ {total}')
            suco = suco + total
            R = input('Deseja continuar ?')  
    else:
           print('ERRO! Escolha um número válido')
           R = input('Deseja continuar ?')

compra = coxinha + pastel + suco + cafe
print (f'Compra finalizada! Ao todo, pagarás R$ {compra}')