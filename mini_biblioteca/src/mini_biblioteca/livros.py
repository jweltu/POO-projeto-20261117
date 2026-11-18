class Livro:
    def __init__(self, titulo, autor, codigo, disponivel=True):
        self.titulo = titulo
        self.autor = autor
        self.codigo = codigo
        self.disponivel = disponivel

    def __str__(self):
        return f"Título - {self.titulo}, Autor - {self.autor}, código - {self.codigo}."
