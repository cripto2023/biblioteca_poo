from livro.livro_fisico import LivroFisico
from socio.socio import Socio
from biblioteca.biblioteca import Biblioteca

biblioteca = Biblioteca()
socio = Socio ('Francisco', '8888', 'Av. A 110')

def criarLivro (titulo, autor, ano_publi, num_pag):
    livro = LivroFisico()

while True:
    print('-- Bem vindo ao Menu --')
    print('1 - Adicionar Livro')
    print('2 - Remober Livro')
    print('3 - Adicionar Sócio')
    print('4 - Remover Sócio')
    print('5 - Alugar Livro')
    print('6 - Devolver Livro')
    print('7 - Listar Livros')
    print('8 - Listar Sócios')
    opcao = int(input('Selecione a opção: '))

    if opcao == 1:
        titulo = input('Digite o titulo: ')
        autor = input('Digite o autor')
        ano = int(input('Digite o ano'))
        num_pages = int(input('Digite o número de páginas'))

        livro = criarLivro((titulo,autor, ano,num_pag))
        biblioteca.adicionarLivros(livro)
    elif opcao == 2:
        id = input('Digite o id do livro: ')
        if biblioteca.removerLivro(id):
            print('Livro removido com sucesso!')
        else:
            print('Livro não encontrado!')

    elif opcao == 3:
        nome = input('Digite o nome do sócio: ')
        telefone = input('Digite o número do telefone: ')
        endereco = input('Digite o endereco')
        socio_novo = Socio(nome, telefone, endereco)
        biblioteca.adicionarSocio(socio_novo)

    elif opcao == 4:
        id = input('Digite id do sócio: ')
        if biblioteca.adicionarSocio(id):
            print('Sócio removido com sucesso!')
        else:
            print('Id não encontrado!')

    elif opcao == 7:
        biblioteca.listarlivros()
    elif opcao == 8:
        biblioteca.listarSocio()




