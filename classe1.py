'''
nomeclatura PascalCase
'''

# class Pessoa:
#     pass

# p0=Pessoa()
# print(p0)

# p1= Pessoa()
# p1.nome = 'leo'
# p1.sobrenome='serafim'

# print(p1.nome)
# print(p1.sobrenome)

# class Pessoa:
#     nome = None
#     def metodo(self):

class Pessoa:

    def __init__(self, nome, sobrenome):
        self.nome=nome
        self.sobrenome=sobrenome

p1= Pessoa('Leo', 'Serafim')

print(p1)
