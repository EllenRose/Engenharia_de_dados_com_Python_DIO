## Otimizando o Sistema Bancário com Python 
## Separação das operações : Depósito ,Saque e Extrato em funções 
## Criando duas novas funções usuário e conta corrente 


# Menu
def menu():
    return """
    === SEJA BEM VINDO AO MENU ===
    [0] Depositar
    [1] Sacar
    [2] Extrato
    [3] Criar usuário
    [4] Criar conta corrente
    [5] Sair
    """

# Criação de novo usuário e lista de usuários
def criar_usuario(usuarios):
    cpf = input("Digite o CPF (apenas números): ")
    nome = input("Digite o nome do usuário: ")
    data_nascimento = input("Digite a data de nascimento (dd/mm/aaaa): ")
    endereco = input("Digite o endereço (logradouro, bairro, cidade/sigla do estado): ")

    # Verificação se o CPF já existe
    if any(usuario['cpf'] == cpf for usuario in usuarios):
        print("CPF já cadastrado!")
        return usuarios

    # Adicionando dicionário
    usuarios.append({ 'nome': nome, 'data_nascimento': data_nascimento, 'cpf': cpf,  'endereco': endereco})

    print("Usuário criado com sucesso!")
    return usuarios

# Criação de conta corrente e vinculação ao usuário
def criar_conta_corrente(contas, usuarios):
    cpf = input("Digite o CPF do usuário  (apenas números): ")
    
    if not any(usuario['cpf'] == cpf for usuario in usuarios):
        print("Usuário não localizado!. Crie um usuário antes de criar uma conta.")
        return contas

    # Criação de um número de conta sequencial , toda vez que criar uma conta será somado 1
    numero_conta = len(contas) + 1
    
    # Agência deve ter número fixo
    AGENCIA = "0001"
    
    conta = { 'numero_conta': numero_conta, 'agencia': AGENCIA,'cpf_usuario': cpf }

    # Adiciona a conta criada à lista de contas
    contas.append(conta)
    print(f"Conta criada com sucesso! Número da conta: {numero_conta}, Agência: {AGENCIA}")
    return contas

# Depositar
def deposito(saldo, valor, extrato, contas, usuarios, cpf_usuario, /):

    # Verifica se o usuário tem uma conta
    if not any(conta['cpf_usuario'] == cpf_usuario for conta in contas):
        print("Conta não cadastrada. Crie uma conta antes de realizar depósitos.")
        return saldo, extrato

    if valor <= 0:
        print("Valor inválido!")
    else:
        saldo += valor
        conta = next(conta for conta in contas if conta['cpf_usuario'] == cpf_usuario)
        nome_usuario = next(usuario['nome'] for usuario in usuarios if usuario['cpf'] == cpf_usuario)
        extrato += (f"Depósito: R$ {valor:.2f}\n"
                    f"Conta: {conta['numero_conta']} - Agência: {conta['agencia']}\n"
                    f"Nome: {nome_usuario}\n"
                    "\n")
        print("\n Depósito realizado com sucesso!\n")
    
    return saldo, extrato

# Sacar
def saque(*, saldo, valor, extrato, limite, numero_saque, LIMITE_SAQUE, contas, usuarios, cpf_usuario):

    # Verifica se o usuário tem uma conta
    if not any(conta['cpf_usuario'] == cpf_usuario for conta in contas):
        print("Conta não cadastrada. Crie uma conta antes de realizar saques.")
        return saldo, extrato, numero_saque

    if numero_saque >= LIMITE_SAQUE:
        print("Número de saques diários excedido!.\n")
    
    elif valor > limite:
        print("O limite máximo para saques diários é de R$ 500.00.\n")
    
    elif saldo < valor:
        print("Saldo insuficiente!\n")
    
    elif valor <= 0:
        print("Valor incorreto!\n")
        
    else:
        saldo -= valor
        conta = next(conta for conta in contas if conta['cpf_usuario'] == cpf_usuario)
        nome_usuario = next(usuario['nome'] for usuario in usuarios if usuario['cpf'] == cpf_usuario)
        extrato += (f"Saque: R$ {valor:.2f}\n"
                    f"Conta: {conta['numero_conta']} - Agência: {conta['agencia']}\n"
                    f"Nome: {nome_usuario}\n"
                    "\n")
        print("\n Operação realizada com sucesso!\n")
        numero_saque += 1

    return saldo, extrato, numero_saque

# Extrato
def extrato(saldo, /, *, extrato):
    """
    Exibe o extrato da conta.
    """
    print("# Extrato da conta #".center(36, "-"))
    print("\nNão foram realizadas movimentações." if not extrato else extrato)
    print(f"\nValor Total em conta: Saldo: R$ {saldo:.2f} \n")
    print("## ## ##".center(36, "-"))

# Código principal que executa o menu e chama as outras funções conforme a opção escolhida
def main():
    # Variáveis
    saldo = 0
    limite = 500
    extrato_banco = ""
    numero_saque = 0
    LIMITE_SAQUE = 3
    # Lista para armazenamento  dos usuários
    usuarios = [] 
    # Lista para armazenamento das contas correntes 
    contas = []   

    while True:
        opcao = input(menu())
        
        # Depósito
        if opcao == "0":
            cpf_usuario = input("Digite o CPF (apenas números): ")
            cpf_usuario = ''.join(filter(str.isdigit, cpf_usuario))
            saldo, extrato_banco = deposito(
                saldo,
                float(input("Informe o valor do depósito: ")),
                extrato_banco,
                contas,
                usuarios,
                cpf_usuario
            )

        # Saque 
        elif opcao == "1":
            cpf_usuario = input("Digite o CPF do usuário: ")
            cpf_usuario = ''.join(filter(str.isdigit, cpf_usuario))
            saldo, extrato_banco, numero_saque = saque(
                saldo=saldo,
                valor=float(input("Informe o valor do saque: ")),
                extrato=extrato_banco,
                limite=limite,
                numero_saque=numero_saque,
                LIMITE_SAQUE=LIMITE_SAQUE,
                contas=contas,
                usuarios=usuarios,
                cpf_usuario=cpf_usuario
            )
        
        # Extrato
        elif opcao == "2":
            extrato(saldo, extrato=extrato_banco)
        
        # criar usuario
        elif opcao == "3":
            usuarios = criar_usuario(usuarios)
        
        # criar conta corrente
        elif opcao == "4":
            contas = criar_conta_corrente(contas, usuarios)
        
        #sair do sistema
        elif opcao == "5":
            print("Obrigado por utilizar nossos canais. Até breve!")
            break
        
        # Nenhuma das opções
        else:
            print("Opção inválida. Por favor, selecione novamente a opção desejada.\n")
