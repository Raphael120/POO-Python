# Comparações e Estendendo objetos do Python:


# class Conta:
#     def __init__(self, id_conta, saldo):
#         self.ID = id_conta
#         self.saldo = saldo
#
#     def deposito(self, valor):
#         self.saldo += valor
#
#     def saque(self, valor):
#         if self.saldo >= valor:
#             self.saldo -= valor
#
#     def __le__(self, other):
#         if self.ID <= other.ID:
#             return True
#         else:
#             return False
#
#     def __eq__(self, other):
#         # return self.ID == other.ID
#         if self.ID == other.ID:
#             return True
#         else:
#             return False
#
#     def __ge__(self, other):
#         if self.ID >= other.ID:
#             return True
#         else:
#             return False
#
#     def __lt__(self, other):
#         if self.ID < other.ID:
#             return True
#         else:
#             return False
#
#     def __gt__(self, other):
#         if self.ID > other.ID:
#             return True
#         else:
#             return False
#
#     def __ne__(self, other):
#         if self.ID != other.ID:
#             return True
#         else:
#             return False
#
#
# class Contas(list):
#     """Classe para ordenar as contas pelo ID em ordem crescente"""
#     def sorteia(self):
#         copia = self.copy()
#         tamanho = len(self)
#         self.clear()
#         while len(self) < tamanho:
#             min_id = copia[0]
#             for conta in copia:
#                 if conta.ID < min_id.ID:
#                     min_id = conta
#             self.append(min_id)
#             copia.remove(min_id)
#
#
# class Banco:
#     def __init__(self):
#         self.contas = Contas()
#
#
# objetoBanco = Banco()
# itau = Conta(123, 4000)
# bradesco = Conta(456, 5000)
# santander = Conta(789, 6000)
# objetoBanco.contas.append(itau)
# objetoBanco.contas.append(santander)
# objetoBanco.contas.append(bradesco)
# objetoBanco.contas.sorteia()
# print(objetoBanco.contas[0].ID)

# print(itau == bradesco)
# itau2 = Conta(123, 4000)
# print(itau == itau2)
# itau3 = itau
# print(itau == itau3)

# Métodos de comparações:
# __le__ --> x <= y
# __eq__ --> x == y
# __ge__ --> x >= y
# __lt__ --> x < y
# __gt__ --> x > y
# __ne__ --> x != y
