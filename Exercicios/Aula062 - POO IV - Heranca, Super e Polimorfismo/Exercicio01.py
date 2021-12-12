"""Defina uma nova classe ObjetoGrafico subclasse de object, cujos atributos são:
- cor_de_preenchimento -> inteiro
- preenchida -> bool
- cor_de_contorno -> inteiro

Escreva três classes:
- Retangulo -> Atributos: base e altura
- Circulo -> Atributos: raio
- Triangulo -> Atributos: base e altura

Subclasses da classe ObjetoGrafico que possuam todas métodos area e perimetro
"""


class ObjetoGrafico(object):
    def __init__(self, cor_de_preenchimento=0, preenchida=True, cor_de_contorno=0):
        self.cor_de_preenchimento = cor_de_preenchimento
        self.preenchida = preenchida
        self.cor_de_contorno = cor_de_contorno


class Retangulo(ObjetoGrafico):
    def __init__(self, base=0, altura=0):
        super(Retangulo, self).__init__()
        self.base = base
        self.altura = altura
        
    def area(self):
        return f'Área do Retângulo: {self.base * self.altura}'
    
    def perimetro(self):
        return f'Perímetro do Retângulo: {2 * (self.base + self.altura)}'
        

objetoRetangulo = Retangulo(5, 10)
print(objetoRetangulo.area())
print(objetoRetangulo.perimetro())
print()


class Circulo(ObjetoGrafico):
    def __init__(self, raio=0):
        super(Circulo, self).__init__()
        self.raio = raio
        
    def area(self):
        return f'Área do Círculo: {3.14 * (self.raio ** 2)}'
    
    def perimetro(self):
        return f'Perímetro do Círculo: {2 * 3.14 * self.raio:.1f}'


objetoCirculo = Circulo(5)
print(objetoCirculo.area())
print(objetoCirculo.perimetro())
print()


class Triangulo(ObjetoGrafico):
    def __init__(self, base=0, altura=0):
        super(Triangulo, self).__init__()
        self.base = base
        self.altura = altura
        
    def area(self):
        return f'Área do Triângulo: {(self.base * self.altura) / 2}'
    
    def perimetro(self):
        return f'Perímetro do Triângulo (equilátero): {self.base * 3}'
    
    
objetoTriangulo = Triangulo(10, 13)
print(objetoTriangulo.area())
print(objetoTriangulo.perimetro())
