lista_livro = dict()
livros = list()
id_global = 0

def cadastrar_livro():
    print('-' * 64)
    print('-' * 20, ' MENU CADASTRAR LIVRO ', '-' * 20)
    lista_livro['nome'] = (input('Por favor entre com o nome do livro:'))
    lista_livro['autor(a)'] = input('Por favor entre com o(a) autor(a) do livro:')
    lista_livro['editora']  = input('Por favor entre com a editora do livro:')
    livros.append(lista_livro.copy())

cadastrar_livro()

print(livros)