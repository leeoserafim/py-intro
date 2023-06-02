class Carro:
    def __init__(self, nome, marca='VW'):
        self.nome=nome
        self.marca=marca

    def acelerar(self):
        print(f'Carro {self.nome} está acelerando')
    def freiar (self):
        print(f'Carro {self.nome} esta freiando')
    def __str__(self):
        return f'Nome: {self.nome} Marca: {self.marca}'
    
fusca = Carro('fusca')
print(fusca.nome)
fusca.acelerar()
fusca.freiar()

focus= Carro(marca=f'ford', nome='focus')

print(focus)
print(fusca) 