# Métodos getter e setter:


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


# @property - Getters e Setters:


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    
    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * (percentual / 100))
        
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, valor):
        self._nome = valor.title()
        
    # Getter
    @property
    def preco(self):
        return self._preco
    
    # Setter
    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace('R$', ''))
            
        self._preco = valor


p1 = Produto('CAMISETA', 50)
p1.desconto(10)
print(p1.nome, p1.preco)

p2 = Produto('caneca', 'R$15')
p2.desconto(10)
print(p2.nome, p2.preco)
