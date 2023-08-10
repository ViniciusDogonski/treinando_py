
import textwrap

# class conta :

#     def __init__(self, nome: str, valor_conta : float):
#         self.nome =nome
#         self.valor_conta =valor_conta
#         self.depositos = 0 

#     def extrato(self):
#         print('--------------------')
#         print('nome')
#         print(self.nome)
#         print('valor da conta')
#         print(self.valor_conta)
#         print('valor de depositos')
#         print(self.depositos)

#     def deposito(self, valor: float):
#         self.valor_conta = self.valor_conta + valor
#         self.depositos = self.depositos + valor

#     def saque(self,valor : float):
#         self.valor_conta = self.valor_conta - valor

class Conta:
    def __init__(self, usuario, limite_para_saques, saldo_limite):
        self.usuario = usuario
        self.limite_para_saques = limite_para_saques
        self.saldo_limite = saldo_limite
        self.extrato = []
        self.numero_de_saques_efetuados = 0

    def realizar_saque(self, valor):
        if self.numero_de_saques_efetuados < self.limite_para_saques and valor <= self.saldo_limite:
            self.saldo_limite -= valor
            self.extrato.append(f"Saque: -{valor}")
            self.numero_de_saques_efetuados += 1
            return True
        else:
            return False

    def depositar(self, valor):
        self.saldo_limite += valor
        self.extrato.append(f"Depósito: +{valor}")

    def consultar_saldo(self):
        return self.saldo_limite

    def consultar_extrato(self):
        return self.extrato
    
    def __str__(self):
        to_print = f"{self.usuario} /"
        return to_print


class Usuario:
    def __init__(self, nome, cpf):
        self._nome = nome
        self._cpf = cpf

    # Método getter para o atributo 'nome'
    def get_nome(self):
        return self._nome

    # Método setter para o atributo 'nome'
    def set_nome(self, novo_nome):
        self._nome = novo_nome

    # Método getter para o atributo 'cpf'
    def get_cpf(self):
        return self._cpf

    # Método setter para o atributo 'cpf'
    def set_cpf(self, novo_cpf):
        self._cpf = novo_cpf
    
    def __str__(self):
        to_print = f"{self._cpf} , {self._nome} /"
        return to_print



# conta1 = conta("nome test", 1000.0)
# conta1.extrato()
# conta1.deposito(200.00)
# conta1.extrato()
# conta1.saque(200.00)
# conta1.extrato()

def menu():
    menu = """\n
        ===============Menu===============
        [d]Depositar
        [s]Sacar
        [e]Extrato
        [nc]Nova Conta
        [lc]Listar Contas
        [nu]Novo Usuário
        [q]Sair
    =>"""
    return input(textwrap.dedent(menu))


def encontrar_conta_por_cpf(lista_de_contas, cpf_alvo):
    for conta in lista_de_contas:
        if conta.usuario.cpf == cpf_alvo:
            return conta
    return None  # Retorna None se nenhuma conta com o CPF for encontrada



def main():
    
    usuarios = []
    contas =[]
    usuarios_sem_conta = [usuario for usuario in usuarios if not any(conta.usuario == usuario for conta in contas)]

    while True:
       opcao = menu()
       match opcao :
        case "d":
            cpf_desejado = int(input("informe o cpf para entrar na conta:"))
            conta_encontrada : Conta = encontrar_conta_por_cpf(contas, cpf_desejado)
            print(conta_encontrada)
            valor = float(input("informe o valor de deposito"))        
            conta_encontrada.depositar(valor)
        case "s":
            print("ass")
        case "e":
            cpf_desejado = int(input("informe o cpf para entrar na conta:"))
            conta_encontrada : Conta = encontrar_conta_por_cpf(contas, cpf_desejado)
            print(conta_encontrada.consultar_extrato)
        case "nc":
            print("ass")
        case "lc":
            print("ass")
        case "nu":
            nome = str(input("informe o nome"))
            cpf = int(input("informe o cpf"))
            novo_usuario = Usuario(nome, cpf)
            usuarios.append(novo_usuario)
            for user in usuarios:
                print(user)
        case "q":
            print("ass")
       





main()