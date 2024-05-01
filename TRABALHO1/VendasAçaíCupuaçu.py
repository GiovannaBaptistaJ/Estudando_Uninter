#APP DE VENDAS PARA EMPRESA X QUE VENDE AÇAÍ E CUPUAÇU
#Tamanho P de Cupuaçu (CP) custa 9 reais e o Açaí (AC) custa 11 reais;
#Tamanho M de Cupuaçu (CP) custa 14 reais e o Açaí (AC) custa 16 reais;
#Tamanho G de Cupuaçu (CP) custa 18 reais e o Açaí (AC) custa 20 reais;

print('Bem-vindo(a) a loja de Gelados da Giovanna!')
print('-' * 20, 'Cardápio', '-' *21)
print('-' * 51)
print('-' * 3, '|', ' Tamanho ', '|', ' Cupuaçu (CP) ', '|', ' Açaí(AC) ', '|','-' * 3)
print('-' * 3, '|', '    P    ', '|', '    R$ 9.00   ', '|', ' R$ 11.00 ', '|','-' * 3)
print('-' * 3, '|', '    M    ', '|', '    R$ 14.00  ', '|', ' R$ 16.00 ', '|','-' * 3)
print('-' * 3, '|', '    G    ', '|', '    R$ 18.00  ', '|', ' R$ 20.00 ', '|','-' * 3)
print('-' * 51)

acumulador = 0 # Variável para armazenar valor da compra

while True:
    sabor = input('Entre com o sabor desejado: (CP/AC)') #Armazena o sabor desejado
    while sabor != 'CP' and sabor != 'AC': #Verifica se o sabor desejado é valido
        print ('Sabor inválido. Tente novamente!')
        sabor = input('Entre com o sabor desejado: (CP/AC)')

    tamanho = input('Digite o tamanho desejado (P/M/G)') #Armazena o tamanho desejado
    while tamanho != 'P' and tamanho != 'M' and tamanho != 'G': #Verifica se o tamanho desejado é valido
        print ('Tamanho inválido. Tente novamente!')
        tamanho = input('Digite o tamanho desejado (P/M/G)')

    if sabor == 'CP': #Verifica o sabor desejado
        if tamanho == 'P': # Verifica o tamanho
            print(f'Você pediu cupuaçu no tamanho P: R$ 9.00')
            acumulador = acumulador + 9.00
        elif tamanho == 'M': # Verifica o tamanho
            print(f'Você pediu cupuaçu no tamanho M: R$ 14.00')
            acumulador = acumulador + 14.00
        else: # Verifica o tamanho
            print(f'Você pediu cupuaçu no tamanho G: R$ 18.00')
            acumulador = acumulador + 18.00
    elif sabor == 'AC': #Verifica o sabor desejado
        if tamanho == 'P': # Verifica o tamanho
            print(f'Você pediu açaí no tamanho P: R$ 11.00')
            acumulador = acumulador + 11.00
        elif tamanho == 'M': # Verifica o tamanho
            print(f'Você pediu açaí no tamanho M: R$ 16.00') 
            acumulador = acumulador + 16.00
        else: # Verifica o tamanho
            print(f'Você pediu açaí no tamanho G: R$ 20.00')
            acumulador = acumulador + 20.00

    perg = input('Deseja pedir mais alguma coisa? S/N')
    while perg != 'S' and perg != 'N':
        print('ERRO! Digite entre S ou N')
        perg = input('Deseja pedir mais alguma coisa? S/N')

    if perg == 'S':
        continue
    else:
        break

print(f'O valor total a ser pago: R$ {acumulador}')
