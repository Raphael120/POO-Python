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


"""
Mais exemplos de Encapsulamento:
public, protected, private <- Outras línguagens
_  <- 'protected'
__ <- 'private | para acessar: (_NomeDaClasse__nomeatributo)'
"""


class BaseDeDados:
    def __init__(self):
        self.__dados = {}
    
    @property  # pode ser utilizado um método para acessar os valores do atributo privado.
    def dados(self):
        return self.__dados
    
    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})
    
    def lista_clientes(self):
        for k, v in self.__dados['clientes'].items():
            print(k, v)
    
    def apaga_cliente(self, id):
        del self.__dados['clientes'][id]


bd = BaseDeDados()
# bd.dados = 'Alguma coisa'  # caso a base de dados fosse alterada, quebraria a classe inteira.
bd.inserir_cliente(1, 'Raphael')
bd.inserir_cliente(2, 'Silva')
bd.inserir_cliente(3, 'Araújo')
# bd.apaga_cliente(2)
# print(bd.__dados)
# print(bd._BaseDeDados__dados) --> pode ser usado para acessar atributos privados.
# bd.lista_clientes()
# print(bd.dados) -> Com o método dados criado, é possivel ter acesso às informações contidas no dicionário dados.
