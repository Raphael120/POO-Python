"""Escreva um programa de bancos que possua:
-> Uma classe Banco com os atributos:
    - private total
    - public taxa_reserva
    - private reserva_exigida
    
    E métodos:
    - private calcula_reserva
    - public pode_fazer_emprestimo(valor) --> bool

-> E uma classe Conta com os atributos
    - private saldo
    - private id_conta
    - private senha
    
    E métodos:
    - public deposito(senha, valor)
    - public saque(senha, valor)
    - public pode_receber_emprestimo(valor) --> bool
    - public saldo --> float
"""


class Banco:
    __total = 50000
    taxa_reserva = 0.1
    __reserva_exigida = __total * taxa_reserva
    
    def __calcula_reserva(self):
        return f'Reserva: R${self.__total * self.taxa_reserva:.2f}'
    
    def pode_fazer_emprestimo(self, valor):
        if valor < self.__total - self.__reserva_exigida:
            return f'O banco pode fazer o empréstimo de R${valor:,.2f} solicitado.'
        else:
            return 'O Banco não tem reservas suficientes para realizar o empréstimo.'


objetoBanco = Banco()
print(objetoBanco.pode_fazer_emprestimo(45001))


class Conta(Banco):
    __saldo = 10000
    __id_conta = 123
    __senha = 12345

    def deposito(self, senha, valor):
        if senha == self.__senha:
            self.__saldo += valor
            return f'Depósito de R${valor:,.2f} realizado com sucesso.'
        else:
            return 'Erro ao realizar depósito\nSENHA INVÁLIDA.'

    def saque(self, senha, valor):
        if senha == self.__senha:
            if valor > self.__saldo:
                return 'Erro ao sacar, saldo insuficiente.'
            else:
                self.__saldo -= valor
                return f'Foi sacado R${valor:,.2f}'
        else:
            return 'Erro ao sacar.\nSENHA INVÁLIDA.'

    def pode_receber_emprestimo(self, valor):
        return self.pode_fazer_emprestimo(valor)

    def saldo(self):
        return f'Saldo atual: R${self.__saldo:,.2f}'


objetoConta = Conta()
# print(objetoConta.deposito(12345, 6000))
print()
print(objetoConta.saque(12345, 1500))
print()
print(objetoConta.saldo())
print()
print(objetoConta.pode_receber_emprestimo(20000))
