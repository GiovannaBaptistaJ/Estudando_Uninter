#SOFTWARE GERENCIAMENTO DE LIVROS
# MENU E OPÇÕES:
#Cadastrar Livro 
#Consultar Livro 
#Consultar Todos  
#Consultar por Id 
#Consultar por Autor 
#Retornar ao menu 
#Remover Livro 
#Encerrar Programa 

print('Bem-vindo(a) a Livraria da Giovanna!')
print('-' * 58)
print('-' * 20, ' MENU PRINCIPAL ', '-' *20)
print('Escolha a opção desejada:')
print('1 - Cadastrar Livro')
print('2 - Cadastrar Livro(s)')
print('3 - Remover Livro')
print('4 - Sair')
opcao = int(input(''))

if opcao >= 5:
     print('Erro!Digite um número entre 1 e 4')

lista_livro = ()
id_global = 0

def cadastrar_livro(id):
    nome = input('Por favor entre com o nome do livro:')
    nome = input('Por favor entre com o autor do livro:')
    nome = input('Por favor entre com a editora do livro:')