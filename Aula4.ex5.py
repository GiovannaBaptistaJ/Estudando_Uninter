#CINEMA

print('CINEMA [Ú]NICO')

perg = input('Desejas verificar o preço dos ingressos? S / N ')
total = 0
totalpessoas = 0
idadepessoas = 0

while perg.upper() =='S':
    idade = int(input('Qual a sua idade?'))
    if (idade < 3):
        print('INGRESSO GRATUITO!')
        total = total + 0
        totalpessoas = totalpessoas + 1
        idadepessoas = idadepessoas + idade  
    elif idade <= 12:
        print('INGRESSO - R$ 15,00')
        total = total + 15.00
        totalpessoas = totalpessoas + 1
        idadepessoas = idadepessoas + idade      
    else:
        print('INGRESSO - R$ 30,00')
        total = total + 30.00
        totalpessoas = totalpessoas + 1
        idadepessoas = idadepessoas + idade
        
perg = input('Deseja verificar outra idade?')


media = idadepessoas / totalpessoas
print(f'Total de pessoas: {totalpessoas}')
print(f'Total do dinheiro arrecadado: {total}')
print(f'Média de idade das pessoas: {media}')

