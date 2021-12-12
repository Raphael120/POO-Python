# class Cubo:  # -> Cabeçalho da classe.
#
#     """Classe para calcular ocudo de um número."""  # -> Docstring.
#
#     # dado = valor --> dado de classe compartilhado (atributo de classe)
#     def __init__(self, valor):  # -> Método construtor.
#         self.x = valor  # -> Dado de instância ('self').
#         print('Objeto criado!')
#
#     def calcula_cubo(self):  # -> Método geral.
#         cubo = self.x ** 3
#         return f'Cubo calculado: {cubo}'
#
#
# # print(type(Cubo))
# teste = Cubo(5)
# c = teste.calcula_cubo()
# print(c)

"""--------------------------------------------------------------------"""

# Método construtor __init__:

# class Gato:
#     """Classe para trabalhar com gatos."""
#
#     def __init__(self, nome):
#         """Inicializa o objeto capturando o nome do animal."""
#         self.nome = nome
#         print(f'O nome do gato é {self.nome}.')
#
#
# nome_gato = str(input('Digite o nome do gato: ')).title().strip()
# g1 = Gato(nome_gato)

"""--------------------------------------------------------------------"""

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

"""--------------------------------------------------------------------"""


# Variáveis de Classe e de Instância:

# class Gato:
#     tipo_animal = 'Felino'
#
#     def __init__(self, nome):
#         self.nome = nome
#
#
# Gato.tipo_animal = 'Pet'
#
# g1 = Gato('Kiki')
# g2 = Gato('Cookie')
#
# print(g1.nome)
# print(g2.nome)
#
# g1.tipo_animal = 'Mascote'
# print(g1.tipo_animal)
# print(g2.tipo_animal)

"""--------------------------------------------------------------------"""
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

"""--------------------------------------------------------------------"""
# Método getter e setter:


# class Teste:
#     def __init__(self, valor):
#         self.x = valor
#
#     def get_valor(self):
#         """Método getter para retornar o valor do atributo x"""
#         return self.x
#
#     def set_valor(self, novo_valor):
#         """Método setter para atribuir um novo valor ao atributo x"""
#         self.x = novo_valor
#
#
# teste = Teste(10)
# print(f'Valor do objeto: {teste.get_valor()}')
#
# v = int(input('Digite um número inteiro: '))
# teste.set_valor(v)
# print(f'Valor do objeto após atribuição: {teste.get_valor()}')

"""--------------------------------------------------------------------"""
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

"""--------------------------------------------------------------------"""
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

"""--------------------------------------------------------------------"""
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


class Conta(object):
    # total = 1000
    __total = 1000  # Encapsulamento (atributo privado)
    reserva = 0.1
    
    def __init__(self, id_conta, saldo):
        self.__id_conta = id_conta  # Encapsulamento (atributo privado)
        self.saldo = saldo
        
    def deposito(self, valor):
        self.saldo += valor
        Conta.__total += self.saldo
        
    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            Conta.__total -= valor
        Conta.__imprimeReserva()
        
    def __imprimeReserva():  # Método privado
        print(Conta.__total * Conta.reserva)
            
            
objetoNubank = Conta(122, 7500)
objetoNubank.deposito(2500)
objetoNubank.saque(4000)
print(objetoNubank.saldo)

# Conta.__imprimeReserva()  # Métodos e atributos privados ficam inacessíveis fora da classe.
