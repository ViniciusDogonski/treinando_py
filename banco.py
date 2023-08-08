
class conta :

    def __init__(self, nome: str, valor_conta : float):
        self.nome =nome
        self.valor_conta =valor_conta
        self.depositos = 0 

    def extrato(self):
        print('--------------------')
        print('nome')
        print(self.nome)
        print('valor da conta')
        print(self.valor_conta)
        print('valor de depositos')
        print(self.depositos)

    def deposito(self, valor: float):
        self.valor_conta = self.valor_conta + valor
        self.depositos = self.depositos + valor

    def saque(self,valor : float):
        self.valor_conta = self.valor_conta - valor




conta1 = conta("nome test", 1000.0)
conta1.extrato()
conta1.deposito(200.00)
conta1.extrato()
conta1.saque(200.00)
conta1.extrato()