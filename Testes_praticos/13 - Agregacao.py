# Agregação (uma classe depende da outra para 'funcionar'):


class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = []
    
    def inserir_produto(self, *produtos):
        for p in produtos:
            self.produtos.append(p)
            
    def lista_produto(self):
        for produto in self.produtos:
            print(produto.nome, produto.valor)
    
    def soma_total(self):
        valor = 0
        for produto in self.produtos:
            valor += produto.valor
            
        return valor


class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor
        
        
objetoCarrinho = CarrinhoDeCompras()

p1 = Produto('Camiseta', 50)
p2 = Produto('iPhone', 10000)
p3 = Produto('Caneca', 15)

objetoCarrinho.inserir_produto(p1, p2, p3, p1, p1, p2, p3)
objetoCarrinho.lista_produto()
print(objetoCarrinho.soma_total())
