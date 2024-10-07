from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime

# Classe Cliente 
class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []
## Realiza uma tranzação 
    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)
## Adiciona a conta recebida por parametro a lista de conta do cliente
    def adicionar_conta(self, conta):
        self.contas.append(conta)

#Classe Pessoa Fisica (estende da classe cliente)
class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

#Classe conta 
class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()
# Retorna uma instância de conta 
    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)
# Retorna o saldo 
    @property
    def saldo(self):
        return self._saldo
#Retorna o número da conta 
    @property
    def numero(self):
        return self._numero
#Retorna a agência 
    @property
    def agencia(self):
        return self._agencia
#Retorna aquele cliente associado a conta 
    @property
    def cliente(self):
        return self._cliente
#Retorna o histórico da conta 
    @property
    def historico(self):
        return self._historico
#Realiza saque da conta 
    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("Saldo Insuficiente")

        elif valor > 0:
            self._saldo -= valor
            print("Operação Realizada com sucesso!")
            return True

        else:
            print("Erro! O valor informado é inválido.")

        return False

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("\n=== Depósito realizado com sucesso! ===")
        else:
            print("Erro! O valor informado é inválido.")
            return False

        return True

# Classe Conta Corrente 
class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques
#Método Saque 
    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__]
        )

        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques >= self.limite_saques

        if excedeu_limite:
            print("Erro! O valor do saque excede o limite!")

        elif excedeu_saques:
            print("Erro! Número de saques excedido!")

        else:
            return super().sacar(valor)

        return False
#Método str ,representação da classe(conta corrente)
    def __str__(self):
        return f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """

# Classe Histórico
class Historico:
    def __init__(self):
        self._transacoes = [] #lista de tranzações
#Propriedades da tranzação 
    @property
    def transacoes(self):
        return self._transacoes
#Método adicionar tranzação 
    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%s"),
            }
        )

#Classe Abstrata de tranzação 
class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self): #propriedade abstrata 
        pass

    @abstractclassmethod
    def registrar(self, conta): #método abstrato , registra tranzação em uma conta 
        pass

# Classe Saque onde representa uma tranzação de saque 
class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self): # retorna o valor de saque 
        return self._valor

    def registrar(self, conta): #registra a tranzação de saque 
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

#Classe depósito 
class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self): #retorna valor de depósito 
        return self._valor

    def registrar(self, conta): # registra operação de depósito 
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)
