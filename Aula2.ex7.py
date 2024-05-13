#CLASSIFICANDO TRIÂNGULOS!
#equilátero : 3 lados iguais
#isósceles: 2 lados iguais
#escaleno: 3 lados diferentes

v1 = int(input('Digite o 1 valor:'))
v2 = int(input('Digite o 2 valor:'))
v3 = int(input('Digite o 3 valor:'))

if (v1 == 0 or v2 == 0 or v3 == 0):
    print('ERRO! Nenhum dos valores pode ser igual a 0')
elif (v1 > v2 + v3 or v2 > v1 + v3 or v3 > v1 + v2):
    print('Erro! Um lado não pode ser maior que a soma dos dois!')
elif (v1 == v2 and v2 == v3):
    print('Triângulo equilátero')
elif (v1 == v2 or v1 == v3 or v2 == v3):
    print('Triângulo isósceles')
elif (v1 != v2 and v1 != v3 and v2 != v3):
    print('Triângulo escaleno')
else:
    print('ERRO')