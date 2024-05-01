#SISTEMA DE COBRANÇA DE SERVIÇOS DE UMA COPIADORA
#Serviço de Digitalização (DIG) o custo por página é de um real e dez centavos;
#Serviço de Impressão Colorida (ICO) o custo por página é de um real; 
#Serviço de Impressão Preto e Branco (IPB) o custo por página é de quarenta centavos; 
#Serviço de Fotocópia (FOT) o custo por página é de vinte centavos; 

#Se número de páginas for menor que 20 retornar o número de página sem desconto;
#Se número de páginas for igual ou maior que 20 e menor que 200 retornar o número de páginas com o desconto é de 15%;
#Se número de páginas for igual ou maior que 200 e menor que 2000 retornar o número de páginas com o desconto é de 20%;
#Se número de páginas for igual ou maior que 2000 e menor que 20000 retornar o número de páginas com o desconto é de 25%;
#Se número de páginas for maior ou igual à 20000 não é aceito pedidos nessa quantidade de páginas;

#Para o adicional de encadernação simples (1) é cobrado um valor extra de 15 reais;
#Para o adicional de encadernação de capa dura (2) é cobrado um valor extra de 40 reais;
#Para o adicional de não querer mais nada (0) é cobrado um valor extra de 0 reais;

print('Bem-vindo(a) a Copiadora da Giovanna!')

def escolha_servico(): #Função para escolher o serviço
    print('Entre com o tipo de serviço desejado!')
    print('DIG - DIGITALIZAÇÃO')
    print('ICO - IMPRESSÃO COLORIDA')
    print('IPB - IMPRESSÃO PRETO E BRANCO')
    print('FOT - FOTOCOPIA')
    servico = input('')
    while servico != 'DIG' and servico != 'ICO' and servico != 'IPB' and servico != 'FOT': #Verificando se o serviço é válido
        print('Escolha inválida, entre com o tipo de serviço novamente')
        servico = input('')
    if servico == 'DIG': #Verificando se o serviço é DIG
        return 1.10
    if servico == 'ICO': #Verificando se o serviço é ICO
        return 1.00
    if servico == 'IPB': #Verificando se o serviço é IPB
        return 0.40
    if servico == 'FOT': #Verificando se o serviço é FOT
        return 0.20
    
def num_pagina(): # Função para escolher número de páginas e aplicar o desconto
    while True:
        try:
            paginas = int(input('Entre com o número de páginas:'))
            break
        except ValueError:
            print('Número inválido.  Tente novamente...')
   
    while paginas >= 20000: # Verifica se o número de páginas ultrapassou do limite
        print('Não aceitamos tantas páginas de uma vez.')
        print('Por favor, entre com o número de páginas novamente.')
        paginas = int(input('Entre com o número de páginas:'))
    
    if paginas < 20:
        return paginas
    elif paginas >= 20 and paginas < 200:
        desconto = (15 * paginas) / 100 # Calcula o desconto
        val_descont = paginas - desconto # Calcula o valor com desconto
        return val_descont
    elif paginas >= 200 and paginas < 2000:
        desconto = (20 * paginas) / 100 # Calcula o desconto
        val_descont = paginas - desconto # Calcula o valor com desconto
        return val_descont
    else:
        desconto = (25 * paginas) / 100 # Calcula o desconto
        val_descont = paginas - desconto # Calcula o valor com desconto
        return val_descont
    
def servico_extra(): # Função para adicionar serviço extra
    print('Deseja adicionar algum serviço?')
    print('1 - Encadernação Simples - R$ 15.00')
    print('2 - Encadernação Capa Dura - R$ 40.00')
    print('0 - Não desejo mais nada')
    while True:
        try:
            adicional = int(input(''))
            break
        except ValueError:
            print('Número inválido.  Tente novamente...')
    while adicional >= 3: # Verifica se a opção escolhida é valida
        print('Erro! Digite um número entre 0 e 2')
        adicional = int(input(''))
    if adicional == 1:
        extra = 15.00 # Adiciona o valor extra
        return extra
    elif adicional == 2:
        extra = 40.00 # Adiciona o valor extra
        return extra
    else:
       extra = 0 # Adiciona nenhum valor
       return extra 

valor_servico = escolha_servico() #Função para escolher o serviço
num_paginas_desconto = num_pagina() # Função para escolher número de páginas e aplicar o desconto
extra = servico_extra() # Função para adicionar serviço extra

if extra == 15.00: #Cálculo do valor total com encadernação simples
        total = (valor_servico * num_paginas_desconto) + 15.00
        print(total)
elif extra == 40.00: #Cálculo do valor total com encadernação Capa Dura
        total = (valor_servico * num_paginas_desconto) + 40.00
else: #Cálculo do valor total caso nenhum serviço extra tenha sido incluido
        total = (valor_servico * num_paginas_desconto)


print (f'Total: R$ {total} (serviço: {valor_servico} * páginas: {num_paginas_desconto} + extra: {extra})')



