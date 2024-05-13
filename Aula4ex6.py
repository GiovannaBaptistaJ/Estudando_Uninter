print('LANÇAMENTO DO FOGUETE')

perg = input('Desejas lançar? S / N ')

if perg == 'S':
    for c in range(10, -1, -1):
        print(c)
else:
    print('FOGUETE NÃO LANÇADO!')

print('FOGO!')