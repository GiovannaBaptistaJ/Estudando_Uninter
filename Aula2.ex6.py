x = 2 + 2
if (x < 4):
    print('True')
else:
    print('False')

x2 = 7 // 3
if (x2 == 1+1):
    print('True')
else:
    print('False')


x3 = 3**2 + 4**2
if (x3 == 25):
    print('True')
else:
    print('False')


x4 = 2 + 4 + 6
if (x4 > 12):
    print('True')
else:
    print('False')


idade = int(input('Qual a sua idade?'))
if (idade > 60):
    print('Você tem direito aos benefícios')
else:
    print('Você não tem direito!')

dano = int(input('Digite o valor do dano'))
escudo = int(input('Digite o valor do escudo'))
if (dano > 10 and escudo == 0):
    print('Você está morto!')
else:
    print('Parabéns, sobreviveu!')

ano = int(input('Em que ano estamos?'))
if (ano % 4 == 0):
    print('Pode ser um ano bissexto')
else:
    print('Definitivamente não é um ano bissexto')

cam = int(input('Escolha um caminho entre 1 e 2'))
if (cam == 1 or cam == 2):
    print('Você decidiu um caminho!')
else:
    print('ERRO!Digite um caminho')