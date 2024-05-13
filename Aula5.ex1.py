
def soma (x, y, z):
    somatorio = x + y + z
    print(f'{somatorio}')

soma (5, 5, 5)

def borda(s1):
    tam = len(s1)

    if tam:
        print('+', '-' * tam, '+')
        print('|',s1,'|')
        print('+', '-' * tam, '+')

borda('Hello Word!')

def contagem (x, y, z):
    for i in range(x, y, z):
        print(i)

contagem (0,6,1)

def valores(x, y, z):
    if x > y and x > z and y > z:
        print(f'Ordem decrescente: {x}, {y}, {z}')
    elif x > y and x > z and z > y:
        print(f'Ordem decrescente: {x}, {z}, {y}')
    elif y > x and y > z and x > z:
        print(f'Ordem decrescente: {y}, {x}, {z}')
    elif y > x and y > z and z > x:
        print(f'Ordem decrescente: {y}, {z}, {x}')
    elif z > x and z > y and x > y:
        print(f'Ordem decrescente: {z}, {x}, {y}')
    elif z > x and z > y and y > x:
        print(f'Ordem decrescente: {z}, {y}, {x}')
    elif z == 0 and x == 0 and z == 0:
        print('Os valores são zero, não existem ordens')
    else:
        print('ERRO! ')

valores(3, 5, 2)