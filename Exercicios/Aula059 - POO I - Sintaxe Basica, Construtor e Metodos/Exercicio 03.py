"""Classe Pessoa: crie uma classe que modele uma pessoa:
Atributos: nome, idade, peso e altura
Métodos: Envelhecer, Engordar, Emagrecer, Crescer.
Obs: por padrão, a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos,
ela deve crescer 0,5cm."""


class Pessoa:
    """Classe que modela uma pessoa seguindo os parâmetros passados."""
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
    
    def envelhecer(self, anos):
        if self.idade < 21:
            return f'\n{self.nome} envelheceu {anos} ano(s) e agora sua altura é {self.altura + (0.5 * anos)}cm\n' \
                   f'Sua nova idade: {self.idade + anos} anos.'
        else:
            return f'\n{self.nome} envelheceu {anos} ano(s) e agora tem {self.idade + anos} anos de idade.'
    
    def engordar(self, kg):
        return f'\n{self.nome} ganhou {kg}kg.\n' \
               f'Seu novo peso: {self.peso + kg}kg'
    
    def emagrecer(self, kg):
        return f'\n{self.nome} perdeu {kg}kg.\n' \
               f'Seu novo peso: {self.peso - kg}kg'
    
    def crescer(self, cm):
        return f'\n{self.nome} cresceu {cm}cm\n' \
               f'Altura anterior: {self.altura}cm\n' \
               f'Nova altura: {self.altura + cm}cm'


pessoa_nome = str(input('Digite seu nome: ')).title().strip()
pessoa_idade = int(input('Digite sua idade: '))
pessoa_peso = float(input('Digite seu peso (kg): '))
pessoa_altura = int(input('Digite sua altura em centímetros (cm): '))

objetoPessoa = Pessoa(pessoa_nome, pessoa_idade, pessoa_peso, pessoa_altura)

print(objetoPessoa.envelhecer(5))
print(objetoPessoa.engordar(5))
print(objetoPessoa.emagrecer(5))
print(objetoPessoa.crescer(4.2))
