## Criação de um sistema bancário com python


## Menu
menu = """

[0] Depositar
[1] Sacar
[2] Extrato
[3] Sair

=> """
## Variáveis
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

## Estrutura
while True:

    opcao = input(menu)
## Depósito
    if opcao == "0":
        valor = float(input("Caro cliente,informe o valor que gostaria de depositar: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Valor inválido!")
## Saque
    elif opcao == "1":
        valor = float(input("Caro cliente, informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Falha durante a operação! Saldo insuficiente.")

        elif excedeu_limite:
            print("Falha durante a opreação!O valor do saque excedeu o seu limite.")

        elif excedeu_saques:
            print("Falha durante a operação!Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Erro! O valor informado é inválido.")
## Extrato
    elif opcao == "2":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "3":
        print (f"Obrigado por utilizar nossos canais.Até breve!\n") 
        break
## Nenhuma das opções acima 
    else:
        print("Falha durante a operação, selecione novamente a operação desejada para darmos continuação.")
