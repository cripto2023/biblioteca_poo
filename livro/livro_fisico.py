from livro.livro import Livro

class LivroFisico(Livro):
    def __init__(self, titulo, autor, ano_publicacao, num_pagina):
        super().__init__(titulo, autor, ano_publicacao)
        self.num_pagina= num_pagina

if __name__ == '__main__':
    livrof = LivroFisico('Harry Potter', 'J K Rolling', 1997, 300)
    print(livrof)