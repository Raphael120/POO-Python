"""Classe Quadrado: crie uma classe que modele um quadrado:
Atributos: Tamanho do lado
Métodos: mudar valor do Lado, retornar valor do lado e calcular área;"""


class Quadrado:
    """Classe que modela um quadrado."""
    def __init__(self, tamanho_do_lado):
        self.x = tamanho_do_lado
        
    def mudar_valor_do_lado(self, novo_valor):
        self.x = novo_valor
    
    def retornar_valor(self):
        return f'Valor do lado: {self.x}'
    
    def calcular_area(self):
        return f'Área do quadrado: {self.x ** 2}'
        

lado = float(input('Tamanho do lado: '))

objetoQuadrado = Quadrado(lado)
print('Valor inicial ->', objetoQuadrado.retornar_valor())

novo_valor_lado = float(input('\nNovo valor do lado: '))

objetoQuadrado.mudar_valor_do_lado(novo_valor_lado)
print('Valor final ->', objetoQuadrado.retornar_valor())

print(objetoQuadrado.calcular_area())
