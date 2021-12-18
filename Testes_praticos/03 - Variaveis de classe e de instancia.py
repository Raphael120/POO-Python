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


class A:
    vc = 123
    
    def __init__(self):
        # vc = 456
        ...


a1 = A()
a2 = A()

A.vc = 'Alterado'

print(a1.vc)
print(a2.vc)
print(A.vc)
