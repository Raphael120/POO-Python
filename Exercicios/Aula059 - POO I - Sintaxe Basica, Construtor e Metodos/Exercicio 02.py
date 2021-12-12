"""Classe Retangulo: crie uma classe que modele um retangulo:
Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
Métodos: mudar valor dos lados, retornar valor dos lados, calcular Área e calcular Perimetro;

-> Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informa as medidas de um local. Depois, deve
criar um objeto com as medidas e calcular a quantidade de pisos necessários para o local."""


class Retangulo:
    """Classe para modelar um Retângulo"""
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        
    def mudar_valor_lados(self, nova_base, nova_altura):
        self.base = nova_base
        self.altura = nova_altura
    
    def retornar_valor_lados(self):
        return f'\nBase do retângulo: {self.base}\n' \
               f'Altura do retângulo: {self.altura}'
    
    def calcular_area(self):
        return f'Área do retângulo: {self.base * self.altura}'
    
    def calcular_perimetro(self):
        return f'Perímetro do retângulo: {2 * (self.base + self.altura)}'
    
    
base_retangulo = float(input('Digite a base do retângulo: '))
altura_retangulo = float(input('Digite a altura do retângulo: '))

objetoRetangulo = Retangulo(base_retangulo, altura_retangulo)

# Mudar valor dos lados:
nova_base_retangulo = float(input('\nDigite um novo valor para a base do retângulo: '))
nova_altura_retangulo = float(input('Digite um novo valor para a altura do retângulo: '))
objetoRetangulo.mudar_valor_lados(nova_base_retangulo, nova_altura_retangulo)

# Retornar valor dos lados, da área  e do perímetro do retângulo:
ladosRetangulo = objetoRetangulo.retornar_valor_lados()
print(ladosRetangulo)

areaRetangulo = objetoRetangulo.calcular_area()
print(areaRetangulo)

perimetroRetangulo = objetoRetangulo.calcular_perimetro()
print(perimetroRetangulo)
