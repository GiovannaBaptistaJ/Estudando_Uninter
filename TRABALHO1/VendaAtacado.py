#APP DE VENDAS PARA EMPRESA X QUE VENDE EM ATACADO
#CONFORME VALOR DA COMPRA, APLICA DESCONTO MAIOR
#Se valor for menor que 2500 o desconto será de 0%;
#Se valor for igual ou maior que 2500 e menor que 6000 o desconto será de 4%;
#Se valor for igual ou maior que 6000 e menor que 10000 o desconto será de 7%;
#Se valor for igual ou maior que 10000 o desconto será de 11%;

print('Bem-vindo(a) a loja da Giovanna!')
val_unit = float(input('Entre com o valor do produto: ')) #Armazena valor do produto
quant_produto = int(input('Digite a quantidade do produto: ')) #Armazena a quantidade do produto
desconto = 0

val_compra = val_unit * quant_produto #Calcula o valor da compra

if val_compra < 2500: #Verifica-se se o valor da compra é menor que 2500
    print('Valor não elegível para desconto!')
    val_descont = val_compra
elif val_compra >= 2500 and val_compra < 6000: #Verifica-se se o valor da compra é igual ou maior que 2500 e menor que 6000
    desconto = (4 * val_compra) / 100 # Calcula o desconto
    val_descont = val_compra - desconto # Calcula o valor com desconto
elif val_compra >= 6000 and val_compra < 10000: #Verifica-se se o valor da compra é igual ou maior que 6000 e menor que 10000
    desconto = (7 * val_compra) / 100 # Calcula o desconto
    val_descont = val_compra - desconto # Calcula o valor com desconto
else: #Verifica-se se o valor da compra é igual ou maior que 10000
    desconto = (11 * val_compra) / 100 # Calcula o desconto
    val_descont = val_compra - desconto # Calcula o valor com desconto

print(f'O valor SEM desconto: R${val_compra}')
print(f'O valor COM desconto: R${val_descont}')



