"""Classe Ponto e Retangulo:
Faça um programa completo utilizando funções e classes que:
-> Possua uma classe chamada Ponto, com os atributos x e y.
-> Possua uma classe chamada Retangulo, com os atributos largura e altura.
-> Possua uma função para imprimir os valores da classe Ponto.
-> Possua uma função para encontrar o centro de um Retângulo.
Você deve criar alguns objetos da classe Retangulo.

- Cada objeto deve ter um vértice de partida, por exemplo, o vértice inferior
esauerdo do retângulo, que deve ser um abjeto da classe Ponto.

- A função para encontrar o centro do retângulo deve retornar o valor para um objeto
do tipo ponto que indique os valores de x e y para o centro do objeto.

- O valor do centro do objeto deve ser mostrado na tela.

- Crie um menu para alterar os valores do retângulo e imprimir o centro deste retângulo."""


class Ponto:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def imprimir(self):
        return f'Valor do ponto x: {self.x}\n' \
               f'Valor do ponto y: {self.y}'


class Retangulo:
    def __init__(self, largura=0, altura=0, vertice=Ponto()):
        self.largura = largura
        self.altura = altura
        self.vertice = vertice

    def encontrar_centro(self):
        x = self.vertice.x + self.largura / 2
        y = self.vertice.y + self.altura / 2
        
        return Ponto(x, y)


objetoRetangulo = Retangulo(7, 19)
objetoPonto = Ponto(objetoRetangulo.encontrar_centro().x, objetoRetangulo.encontrar_centro().y)
print(objetoPonto.imprimir())
