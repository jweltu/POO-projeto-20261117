from emprestimos import Emprestimo
from livros import Livro
from usuarios import Usuario

usuario1 = Usuario("Icaro", 1)
livro1 = Livro("Memórias Póstumas de Brás Cubas", "Machado de Assis", 1)
emprestimo1 = Emprestimo(livro1, usuario1)

emprestimo1.devolver()