from typing import List


class Boletim:
    def __init__(self, nota1, nota2, nota3, nota4):
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
        self.nota4 = nota4
       

    def __str__(self):
        media = (self.nota1 + self.nota2 + self.nota3 + self.nota4)/4
        return f'Nota 1: {self.nota1}, Nota 2: {self.nota2}, Nota 3: {self.nota3}, Nota 4: {self.nota4} e Média: {media}'

