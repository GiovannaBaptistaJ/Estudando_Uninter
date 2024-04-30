# PRATICANDO DICIONÁRIOS
#Média >= 7, aprovado;
#Média < 7 e >= 5, em exame;
# Média < 5, reprovado.

aluno = {}

aluno['nome'] = input('Digite o nome do aluno:')
nota1 = float(input('Digite a primeira nota:'))
nota2 = float(input('Digite a segunda nota:'))
nota3 = float(input('Digite a terceira nota:'))

media = (nota1 + nota2 + nota3) / 3
aluno ['media'] = media

if media >=7 :
    aluno['situação'] = 'Aprovado!'
elif media < 7 and media >=5 :
    aluno['Situação'] = 'Em exame!'
else:
    aluno['Situação'] = 'Reprovado!'

for chave, valor in aluno.items():

  print(f'{chave} = {valor}')


