# Objetos:


# class CalculaCubo:
#     """Classe que permite calcular o cubo de um número"""
#
#     def __init__(self, valor):
#         self.x = valor
#         self.cubo = self.x ** 3
#
#     def calcula_cubo(self):
#         # self.cubo = self.x ** 3  # pode ser colocado no método construtor.
#         return f'O cubo do número {self.x} é: {self.cubo}'
#         # return f'O cubo do número {self.x} é: {self.x ** 3}'   <- Ou sem o atributo 'self.cubo'
#
#
# #  Objeto 1:
# num = int(input('Digite um número inteiro: '))
# objetoCubo = CalculaCubo(num)  # Instanciar a classe
# cubo = objetoCubo.calcula_cubo()
# print(cubo)
#
# #  Objeto 2: (Usa a mesma classe CalculaCubo, só que utiliza um valor diferente)
# num2 = int(input('\nDigite outro número inteiro: '))
# objetoCubo2 = CalculaCubo(num2)  # Instanciar a classe novamente
# cubo2 = objetoCubo2.calcula_cubo()
# print(cubo2)
