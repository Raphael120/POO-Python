# Abstração, Atributo/Métodos estáticos e Encapsulamento:


# class ObjetoGrafico(object):
#     def __init__(self, cor):
#         self.cor = cor
#
#     def area(self):  # Método abstrato
#         pass
#
#     def perimetro(self):  # Método abstrato
#         pass
#
#     def info(self):
#         print(f'{self.area()} m² serão preenchidos com a cor {self.cor}.')
#
#
# class Cachorro:
#     nome = 'Rex'
#     cor = 'Marrom'
#
#
# Dog = Cachorro()
# print(Dog.nome, Dog.cor)
# print(Cachorro.nome, Cachorro.cor)


"""__________________________________________________________________________________________________________________"""
# Encapsulamento:

# class Conta(object):
#     # total = 1000
#     __total = 1000  # Encapsulamento (atributo privado)
#     reserva = 0.1
#
#     def __init__(self, id_conta, saldo):
#         self.__id_conta = id_conta  # Encapsulamento (atributo privado)
#         self.saldo = saldo
#
#     def deposito(self, valor):
#         self.saldo += valor
#         Conta.__total += self.saldo
#
#     def saque(self, valor):
#         if self.saldo >= valor:
#             self.saldo -= valor
#             Conta.__total -= valor
#         Conta.__imprimeReserva()
#
#     def __imprimeReserva():  # Método privado
#         print(Conta.__total * Conta.reserva)
#
#
# objetoNubank = Conta(122, 7500)
# objetoNubank.deposito(2500)
# objetoNubank.saque(4000)
# print(objetoNubank.saldo)

# Conta.__imprimeReserva()  # Métodos e atributos privados ficam inacessíveis fora da classe.


# Mais exemplos de Encapsulamento:
