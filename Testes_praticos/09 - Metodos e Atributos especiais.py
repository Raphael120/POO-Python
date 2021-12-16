# Métodos e Atributos Especiais:


# class Conta:
#     """
#     Classe do tipo conta, representa uma conta num banco qualquer.
#     """
#     def __init__(self, id_conta, saldo):
#         """
#         Contrutor da classe conta.
#         """
#         self.ID = id_conta
#         self.saldo = saldo
#
#     def __str__(self):  # Método que converte um objeto numa string.
#         """
#         Devolve uma string representando a conta.
#         """
#         return f'ID: {self.ID}\nSaldo: R${self.saldo}'
#
#     def __add__(self, other):  # Método que faz a soma entre valores de objetos.
#         """
#         Permite somar uma conta a outra.
#         """
#         # __sub__(), __divmod__(), __mul__(): --> Métodos que também fazem operações entre objetos.
#         self.saldo += other.saldo
#
#     def __call__(self, x):  # torna um objeto "chamável".
#         return x


# ObjetoBradesco = Conta(123, 5000)
# print(callable(ObjetoBradesco))
# print(ObjetoBradesco('teste de objeto chamável'))
# ObjetoItau = Conta(123, 7800)
# ObjetoSantander = Conta(123, 1500)
# # print(str(ObjetoBradesco))
# ObjetoBradesco + ObjetoItau
# print(ObjetoBradesco.saldo)


# class Pai:
#     ...
#
#
# class Filha(Pai):
#     ...
#
#
# class Neta(Filha):
#     ...
#
#
# print(issubclass(Pai, Filha))  # Mostra se uma classe é subclasse da outra.
# print(issubclass(Filha, Pai))
# print(issubclass(Neta, Pai))
# print(Filha.__bases__)  # Mostra a superclasse direta em que foi "herdada".
# print(callable(Pai))  # Mostra se um determinado item é chamável. -> retorna True
# print(callable(10))  # retorna False
