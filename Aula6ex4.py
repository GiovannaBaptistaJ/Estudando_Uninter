
perg = input('Deseja cadastrar? S/N ')
pessoas = []
totalnomes = []
totalimc = []

while perg == 'S':
    nome = input('Digite o nome: ')
    altura = float(input('Digite a altura: '))
    peso = int(input('Digite o peso: '))

    totalnomes.append (nome)
    

    imc = peso / altura ** 2
    totalimc.append (imc)

    pessoas.append([nome, altura, peso, imc])

    perg = input('Deseja cadastrar? S/N ')


tamanhonomes = len(totalnomes)

def func_maior(msg, nums):
    
        maior = max(nums)
        print(msg, maior)

def func_menor(msg, nums):
        menor = min(nums)
        print(msg, menor)

print(f'Cadastros: {pessoas}')
print(f'Total de pessoas cadastradas: {tamanhonomes}')
func_maior('O maior IMC foi de:', totalimc)
func_menor('O menor IMC foi de:', totalimc)





    






