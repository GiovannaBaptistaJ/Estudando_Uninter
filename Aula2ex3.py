#EMPRESA - VERIFICANDO OS BÔNUS DOS FUNCIONÁRIOS
# 30% - FUNCIONÁRIOS DE 10+ ANOS
# 20% - FUNCIONÁRIOS DE 5+ ANOS
# 10% - OUTROS

ano = int(input('Há quantos anos você está na empresa?'))
salario = float(input('Qual seu salário?'))
aumento = 0

if (ano >= 10):
    print('Você tem direito a 30% de bônus! Seu salário será:')
    aumento = (salario * 30) / 100
    salarioatual = salario + aumento
    print(salarioatual)
elif (ano >= 5 and ano <=9):
    print('Você tem direito a 20% de bônus! Seu salário será:')
    aumento = (salario * 20) / 100
    salarioatual = salario + aumento
    print(salarioatual)
else:
    print('Você tem direito a 10% de bônus! Seu salário será:')
    aumento = (salario * 10) / 100
    salarioatual = salario + aumento
    print(salarioatual)