#TERRENOS
print ('1 - RESIDENCIAL 2 - COMERCIAL 3 - INDUSTRIAL')

tip = int(input('Qual o tipo de terreno desejas?'))

if (tip == 1):
    print('1 - ATÉ 500 2 - ACIMA DE 500')
    faixa = int(input('Faixa de até 500 ou acima de 500?'))
    if (faixa == 1):
        print('Preço: 0,40')
    elif (faixa == 2):
        print('Preço de 0,65')
    else:
        print('Erro!Digite entre 1 e 2')

elif (tip == 2):
    print('1 - ATÉ 1000 2 - ACIMA DE 1000')
    faixa = int(input('Faixa de até 1000 ou acima de 1000?'))
    if (faixa == 1):
        print('Preço: 0,55')
    elif (faixa == 2):
        print('Preço de 0,60')
    else:
        print('Erro!Digite entre 1 e 2')
elif (tip == 3):
    print('1 - ATÉ 5000 2 - ACIMA DE 5000')
    faixa = int(input('Faixa de até 5000 ou acima de 5000?'))
    if (faixa == 1):
        print('Preço: 0,55')
    elif (faixa == 2):
        print('Preço de 0,60')
    else:
        print('Erro!Digite entre 1 e 2')
else:
    print('ERRO! Escolha entre 1, 2 ou 3')