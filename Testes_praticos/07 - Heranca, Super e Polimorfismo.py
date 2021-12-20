# Herança, Super e Polimorfismo


# class Mamifero:
#     def __init__(self, cor_de_pelo, genero, num_de_patas):
#         self.cor_de_pelo = cor_de_pelo
#         self.genero = genero
#         self.num_de_patas = num_de_patas
#
#     def falar(self):
#         print('Olá, sou um mamífero e eu sei falar')
#
#     def andar(self):
#         print(f'Estou andando sobre {self.num_de_patas} patas')
#
#     def amamentar(self):
#         if self.genero.upper()[0] == 'M':
#             print('Machos não amamentam')
#         else:
#             print('Amamentando meu filhote')
#
#
# Rex = Mamifero('marrom', 'macho', 4)
# Rex.falar()
# Rex.andar()
# Rex.amamentar()
# print()
#
#
# class Pessoa(Mamifero):
#     def __init__(self, cor_de_pelo, genero, num_de_patas, cabelo):
#         super(Pessoa, self).__init__(cor_de_pelo, genero, num_de_patas)
#         self.cabelo = cabelo
#
#     def falar(self):
#         super(Pessoa, self).falar()
#         print('Olá, sou uma pessoa e eu sei falar')
#
#
# Julia = Pessoa('preta', 'feminino', 2, 'Loiro')
# Julia.falar()
# # Julia.andar()
# # Julia.amamentar()

"""------------------------------------------------------------------------------------------------------------------"""
# Mais exemplos de Herança Simples:


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__
        
    def falar(self):
        print(f'{self.nomeclasse} Falando...')
    

class Cliente(Pessoa):
    def comprar(self):
        print(f'{self.nomeclasse} comprando...')


class Aluno(Pessoa):
    def estudar(self):
        print(f'{self.nomeclasse} estudando...')


c1 = Cliente('Luiz', 45)
c1.falar()
c1.comprar()

a1 = Aluno('Maria', 54)
a1.falar()
a1.estudar()

p1 = Pessoa('João', 43)
p1.falar()
