# Composição (uma classe pertence a outra classe):
# -> Associação - USA | Agregação - TEM | Composição - É DONO | Herança - É <-


class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.enderecos = []
        
    def insere_endereco(self, cidade, estado):
        self.enderecos.append(Endereco(cidade, estado))
        
    def lista_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.cidade, endereco.estado)
            
    def __del__(self):
        print(f'{self.nome} FOI APAGADO')
    
    
class Endereco:
    def __init__(self, cidade, estado):
        self.cidade = cidade
        self.estado = estado
        
    def __del__(self):
        print(f'{self.cidade}-{self.estado} FOI APAGADO')
        
        
objetoCliente1 = Cliente('Luiz', 32)
objetoCliente1.insere_endereco('Belo Horizonte', 'MG')
print(objetoCliente1.nome)
objetoCliente1.lista_enderecos()
# del objetoCliente1
print()

objetoCliente2 = Cliente('Maria', 55)
objetoCliente2.insere_endereco('Salvador', 'BA')
objetoCliente2.insere_endereco('Rio de Janeiro', 'RJ')
print(objetoCliente2.nome)
objetoCliente2.lista_enderecos()
# del objetoCliente2
print()

objetoCliente3 = Cliente('João', 19)
objetoCliente3.insere_endereco('São Paulo', 'SP')
print(objetoCliente3.nome)
objetoCliente3.lista_enderecos()
# del objetoCliente3
print()

print('_______________________')
