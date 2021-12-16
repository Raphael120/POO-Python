# Métodos gerais:

# class Gato:
#     """Classe para trabalhar com gatos."""
#
#     def __init__(self, nome):
#         """Inicializa o objeto capturando o nome do animal."""
#         self.nome = nome
#         print(f'O nome do gato é {self.nome}.\n')
#
#     def peso_gato(self, peso):
#         self.peso = peso
#
#         if self.peso > 5:
#             print('O gato está gordo!')
#         elif self.peso > 3.5:
#             print('O peso do gato está normal.')
#         else:
#             print('O animal está abaixo do peso!')
#
#     def _dieta_especial_gato(self):
#         if self.peso < 3.5:
#             return 'Aumente a ração do felino.'
#         elif self.peso >= 5.0:
#             return 'Diminua a ração do felino.'
#         else:
#             return 'Tudo ok!'
#
#     def dados_gato(self):
#         print(f'O gato {self.nome} está com {self.peso}kg\n')
#         print(self._dieta_especial_gato())
#
#
# nome_gato = str(input('Digite o nome do gato: ')).title().strip()
# g1 = Gato(nome_gato)
#
# peso_do_gato = float(input('Digite o peso do gato (em kg): '))
# g1.peso_gato(peso_do_gato)
# g1.dados_gato()
