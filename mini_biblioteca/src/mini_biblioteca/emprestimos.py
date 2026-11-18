from livros import Livro
from usuarios import Usuario

class Emprestimo:
    def __init__(self, livro: Livro, usuario: Usuario, ativo=True):
        self.livro = livro
        self.usuario = usuario
        self.ativo = ativo
        try:
            self.livro.disponivel = True
            print(f"Emprestimo aceito! \nLivro: {str(livro)} \nUsuário: {str(usuario)}")
        except:
            raise ValueError

    def devolver(self):
        self.ativo = False
        self.livro.disponivel = True
        print(f"\nLivro {self.livro.titulo} devolvido.")
