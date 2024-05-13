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

livro = dict()
lista_livro = list()
id_global = 0

def cadastrar_livro(id_livro): #Cadastro do livro
    print('-' * 58)
    print('-' * 17, ' MENU CADASTRAR LIVRO ', '-' * 17)
    livro['id'] = id_livro # Cria o ID do livro
    print(f'ID do livro: {id_livro}')
    livro['nome'] = input('Por favor entre com o nome do livro:') #Armazena o nome do livro
    livro['autor'] = input('Por favor entre com o autor do livro:') #Armazena o(a) autor(a) do livro
    livro['editora']  = input('Por favor entre com a editora do livro:') #Armazena a editora do livro
    lista_livro.append(livro.copy()) #Adiciona o livro em uma lista

    print('-' * 58)
    print('')

def consultar_livro(): #Consulta de livros
    print('-' * 64)
    print('-' * 20, ' MENU CONSULTAR LIVRO ', '-' *20)
    print('Escolha a opção desejada:')
    print('1 - Consultar Todos os Livros') 
    print('2 - Consultar Livro por ID') 
    print('3 - Consultar Livro(s) por autor') 
    print('4 - Retornar') 
    op = int(input('>>')) #Pergunta qual a opção desejada

    if op != 1 and op != 2 and op != 3 and op != 4: #Verifica se a opção escolhida é válida
        print('-' * 20)
        print('Opção inválida!')
        print('-' * 20)
        consultar_livro()

    elif op == 1: #Consulta todos
       print('-' * 20)
       for liv in lista_livro:
            print(f'id: {liv['id']}')
            print(f'nome: {liv['nome']}')
            print(f'autor: {liv['autor']}')
            print(f'editora: {liv['editora']}')
            print('')

       print('-' * 20)

    elif op == 2: #Consulta por ID
        perg = int(input('Digite o id do livro: ')) #Pergunta o ID desejado

        livros_por_id = {livro["id"]: livro for livro in lista_livro}

        livro_encontrado = livros_por_id.get(perg)

        if livro_encontrado:
            print('-' * 20)
            print(f'id {livro_encontrado['id']}')
            print(f'nome: {livro_encontrado['nome']}')
            print(f'autor: {livro_encontrado['autor']}')
            print(f'editora: {livro_encontrado['editora']}')
            print('')
            print('-' * 20)
        else:
            print('-' * 20)
            print("Livro com ID", perg, "não encontrado.")
            print('-' * 20)

    elif op == 3: #Consulta por autor
            perg = (input('Digite o autor do(s) livro(s): ')) #Pergunta o autor desejado
            print('-' * 20)
            for livro in lista_livro:
                if livro['autor'] == perg:
                    print(f'id: {livro['id']}')
                    print(f'nome: {livro['nome']}')
                    print(f'autor: {livro['autor']}')
                    print(f'editora: {livro['editora']}')
                    print('')
            print('-' * 20)

    else: #Retorna ao menu
       print('Retornando ao menu...')
        
def remover_livro(): # Remoção de livro
    print('-' * 62)
    print('-' * 20, ' MENU REMOVER LIVRO ', '-' *20)
    perg = int(input('Digite o id do livro a ser removido: ')) #Pergunta qual livro removido desejado
    livros_por_id = {livro["id"]: livro for livro in lista_livro}

    livro_encontrado = livros_por_id.get(perg)

    if livro_encontrado:
        lista_livro.remove(livro_encontrado)
        print('Livro removido com sucesso!')
    else:
        print("Livro com ID", perg, "não encontrado.")
        remover_livro()

print('Bem-vindo(a) a Livraria da Giovanna!') 
while True: #Início do programa
    print('-' * 58)
    print('-' * 20, ' MENU PRINCIPAL ', '-' *20)
    print('Escolha a opção desejada:')
    print('1 - Cadastrar Livro')
    print('2 - Consultar Livro(s)')
    print('3 - Remover Livro')
    print('4 - Sair')
    opcao = int(input('>>')) #Pergunta qual a opção desejada

    while opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4: #Verifica se a opção desejada é válida
        print('Erro!Digite um número entre 1 e 4')
        opcao = int(input(''))
    if opcao == 1: #Verifica se o usuário quer cadastrar um livro
        id_global += 1
        cadastrar_livro(id_global)
    elif opcao == 2: #Verifica se o usuário quer consultar um(uns) livro(s)
        consultar_livro()
    elif opcao == 3: #Verifica se o usuário quer remover um livro
        remover_livro()
    else: #Finaliza o programa
        print('Programa finalizado')
        break