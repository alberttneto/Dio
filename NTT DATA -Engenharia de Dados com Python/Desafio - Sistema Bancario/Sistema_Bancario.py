from datetime import datetime, date


## Conta e Usuário
usuarios = []
contas = []

## Funções 

def cadastrar_usuario(usuarios):

    nome = input("\nInforme nome: ")
    data_nascimento = input("Informe data nascimento dd/mm/aa: ")
    cpf = input("Informe cpf: ")

    if(sum([cpf == x["cpf"] for x in usuarios])):
        print("\nUsuario já existe!!")
        return {}
    
    logradouro = input("Informe logradouro: ")
    nro = input("Informe nro: ")
    bairro = input("Informe bairro: ")
    cidade = input("Informe cidade: ")
    estado = input("Informe estado: ")

    return {"nome": nome, 
            "data_nascimento": data_nascimento,
            "cpf": cpf,
            "endereco": {"logradouro": logradouro,
                       "nro": nro,
                       "bairro": bairro,
                       "cidade": cidade,
                       "estado": estado}}


def cadastrar_conta(numero_conta):

    usuario = input("\nInforme CPF do usuário: ")

    return {"conta": numero_conta+1,
            "agencia": "0001",
            "usuario": usuario,
            "saldo": 0}



def deposito():

    valor = float(input("\nInforme valor de deposito: "))
    return valor

def saque(*, qtd_saque, saldo):

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

def extrato(saldo, *, relatorio_extrato):
    if saldo == 0:
        print("\n#### Não foram realizadas movimentações.")
    else:
        data_extrato = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print("{} \n\n ####### Saldo: R$ {:.2f} --- {}".format(relatorio_extrato,saldo, data_extrato))



## Menu

def menu_cadastrar():

    opcao_cadastros = 0
    while opcao_cadastros != 5:

        ## Menu Cadastros
        opcao_cadastros = int(input("""

        1 - Cadastro Usuário
        2 - Cadastro Conta
        3 - Listar Usuários
        4 - Listar Contas
        5 - Voltar

        """))

        if opcao_cadastros == 1:

            novo_usuario = cadastrar_usuario(usuarios)

            if novo_usuario != {}:
                usuarios.append(novo_usuario)
        elif opcao_cadastros == 2:
            if(contas == []):
                contas.append(cadastrar_conta(0))
            else:
                contas.append(cadastrar_conta(contas[len(contas)-1]["conta"]))
        elif opcao_cadastros == 3:
            print("\n")
            for x in usuarios:
                print(x)
        elif opcao_cadastros == 4:
            print("\n")
            for x in contas:
                print(x)
        elif opcao_cadastros == 5:
            print("\n -- Retornando ao menu principal --")
        else:
            print("\n Erro: Opção invalida!")

def menu_acesso_conta(saldo):

    data_hoje = date.today()
    limite_transacoes_diarias = 10
    qtd_saque = 3
    relatorio_extrato = """\n\n ### EXTRATO ### \n"""

    opcao_contas = 0
    while opcao_contas != 4:

        data_transacao = datetime.now()
        data_transacao_formatado = data_transacao.strftime("%d/%m/%Y %H:%M:%S")
        
        if data_transacao.date() != data_hoje:
            limite_transacoes_diarias = 10

        ## Menu Conta
        opcao_contas = int(input("""

        1 - Depositar
        2 - Saque
        3 - Extrato
        4 - Voltar

        """))


        if limite_transacoes_diarias == 0:
            print("\n Limite de transações diarias excedidas! Tente amanhã.")
            

        ## Executa opções
        if opcao_contas == 1 and limite_transacoes_diarias != 0:

            valor_operacao = deposito()
            saldo += valor_operacao
            limite_transacoes_diarias -= 1
            relatorio_extrato += "Deposito: + R$ {:.2f} | Saldo: R$ {:.2f} --- {}\n".format(valor_operacao, saldo, data_transacao_formatado)
        elif opcao_contas == 2 and limite_transacoes_diarias != 0:

            valor_operacao = saque(qtd_saque=qtd_saque, saldo=saldo)
            saldo -= valor_operacao
            if valor_operacao != 0:
                qtd_saque -= 1
                limite_transacoes_diarias -= 1
                relatorio_extrato += "Saque: - R$ {:.2f} | Saldo: R$ {:.2f} --- {}\n".format(valor_operacao, saldo, data_transacao_formatado)

        elif opcao_contas == 3:
            extrato(saldo, relatorio_extrato=relatorio_extrato)
            
        elif opcao_contas == 4:
            print("\n -- Retornando ao menu principal --")

        else:
            print("\n Erro: Opção invalida!")
    
    return saldo

opcao_menu_principal = 0
while opcao_menu_principal != 3:

    ## Menu Principal
    opcao_menu_principal = int(input("""

    1 - Cadastros
    2 - Conta
    3 - Sair

    """)) 

    if opcao_menu_principal == 1:
        menu_cadastrar()
    elif opcao_menu_principal == 2:
        cpf = input("\nInforme CPF do usuario: ")
        conta = int(input("\nInforme conta: "))
        indice_user = [index for (index,value) in enumerate(contas) if cpf == value["usuario"] and conta == value["conta"] ]

        if indice_user == []:
            print("\n Usuario inexistente!!")
        else:
            contas[indice_user[0]]["saldo"] = menu_acesso_conta(contas[indice_user[0]]["saldo"])

    elif opcao_menu_principal == 3:
        print("\n -- Sistema finalizado! --")
    else:
        print("\n Erro: Opção invalida!")






