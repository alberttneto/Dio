
## Variaveis
saldo = 0
qtd_saque = 3
relatorio_extrato = """\n\n ### EXTRATO ### \n"""


## Funções 
def deposito():

    valor = float(input("\nInforme valor de deposito: "))
    return valor

def saque(qtd_saque, saldo):

    limite_saque = 500
    valor = float(input("\nInforme valor de saque: "))

    if valor > limite_saque:
        print("\n Erro: Valor superior ao limite de R$ 500.00\n")
        return 0
    elif valor > saldo:
        print("\n Erro: Valor superior ao saldo de conta de R$ {:.2f}\n".format(saldo))
        return 0
    elif qtd_saque == 0:
        print("\n Erro: Limite de saque diario excedido\n")
        return 0

    return valor

def extrato(saldo, relatorio_extrato):
    if saldo == 0:
        print("\n#### Não foram realizadas movimentações.")
    else:
        print("{} \n\n ####### Saldo: R$ {:.2f}".format(relatorio_extrato,saldo))
        

opcao = 0
while opcao != 4:

    ## Menu
    opcao = int(input("""

    1 - Depositar
    2 - Saque
    3 - Extrato
    4 - Sair

    """))


    ## Executa opções
    if opcao == 1:

        valor_operacao = deposito()
        saldo += valor_operacao
        relatorio_extrato += "Deposito: + R$ {:.2f} | Saldo: R$ {:.2f}\n".format(valor_operacao, saldo)

    elif opcao == 2:

        valor_operacao = saque(qtd_saque, saldo)
        saldo -= valor_operacao
        if valor_operacao != 0:
            qtd_saque -= 1
            relatorio_extrato += "Saque: - R$ {:.2f} | Saldo: R$ {:.2f}\n".format(valor_operacao, saldo)

    elif opcao == 3:
        extrato(saldo, relatorio_extrato)
        
    elif opcao == 4:
        print("\n -- Consulta de conta encerrada! --")

    else:
        print("\n Erro: Opção invalida!")

