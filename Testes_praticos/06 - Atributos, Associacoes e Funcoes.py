# Atributos, Associações e Funçoes:


# class Minha:
#     def __init__(self):
#         self.x = 0
#         self.y = 1
#
#
# objetoMeu = Minha()
# # objetoMeu.x = 3  # --> Pode ser atribuído outros valores para os atributos de uma classe.
# print(objetoMeu.x)

# class PessoaS2Animais:
#     def __init__(self, nome, peso, cao):
#         self.nome = nome
#         self.peso = peso
#         self.cao = cao
#
#     def treinar(self):
#         self.cao.daApatinha()
#         self.cao.latir()
#
#
# class Cachorro:
#     def __init__(self, nome, cor):
#         self.nome = nome
#         self.cor = cor
#
#     def daApatinha(self):
#         print(f'{self.nome} estendeu a pata.')
#
#     def latir(self):
#         return 'AUAU!'
#
#
# rex = Cachorro('Rex', 'marrom')
# raphael = PessoaS2Animais('Raphael', 62, rex)  # -> Associação do objeto 'raphael' com o objeto 'rex'.
# print(raphael.cao)
# print(raphael.cao.cor)  # -> Com a associação, podem ser acessados métodos e atributos de ambas as classes.
# raphael.treinar()
