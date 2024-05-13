#NOME, ANO NASCIMENTO E SEXO

galera = list()

pessoa = dict()

soma = 0

media = 0

fem = 0

while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))

    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] '))
        if pessoa['sexo'] != 'M' and pessoa['sexo'] != 'F':
            print('ERRO! Por favor, digite apenas M ou F')
        else:
            break

    pessoa['idade'] = int(input('Idade: '))

    soma += pessoa ['idade']

    galera.append(pessoa.copy())

    while True:
        resp = str(input('Quer continuar? S/N '))
        if resp != 'S' and resp != 'N':
            print('ERRO! Responda apenas S ou N')
        else:
            break
    if resp == 'S':
        continue
    else:
        break

print('-' * 30)
print(galera)

print(f'Ao todo temos {len(galera)} pessoas cadastradas.')

media = soma / len(galera)
print(f'A média de idade é de {media} anos.')

print('As mulheres abaixo de 30 anos:')
for p in galera:
    if p['sexo'] == 'F' and p['idade'] < 30:
        print(f'{p['nome']}')
print('Os homens com idade acima da media:')
for p in galera:
    if p['sexo'] == 'M' and p['idade'] > media:
        print(f'{p['nome']}')