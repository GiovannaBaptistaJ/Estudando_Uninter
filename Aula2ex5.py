#CALCULADORA

print('Cálculo de 2 valores inteiros!')

n1 = int(input('Digite o 1 valor: '))
n2 = int(input('Digite o 2 valor: '))

print('Digite 1 para adição')
print('Digite 2 para subtração')
print('Digite 3 para multiplicação')
print('Digite 4 para divisão')
oper = int(input('Qual operação aritmética deseja fazer?'))

if (oper == 1):
    calculo = n1 + n2
    print(f'A soma entre os valores {n1} e {n2} resultou {calculo}')
elif (oper == 2):
    calculo = n1 - n2
    print(f'A subtração entre os valores {n1} e {n2} resultou {calculo}')
elif (oper == 3):
    calculo = n1 * n2
    print(f'A multiplicação entre os valores {n1} e {n2} resultou {calculo}')
elif (oper == 4):
    calculo = n1 / n2
    print(f'A divisão entre os valores {n1} e {n2} resultou {calculo}')
else:
    print('Nenhuma operação escolhida. Reinicie o processo')


