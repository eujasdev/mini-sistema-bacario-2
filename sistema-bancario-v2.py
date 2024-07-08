from datetime import datetime

contas = []
agencia = 1313
posicao_da_conta = 0

def tem_conta(menu_cpf_usuario):
    return any(conta["cpf"] == menu_cpf_usuario)
def tem_conta_corrente():
    return any(conta["cpf"] == menu_cpf_usuario and conta.get('conta_corrente', False) for conta in contas)

def solicitar_data_nascimento():
        while True:
            data_de_nascimento_str = input("Data de nascimento para cadastro (DD/MM/AAAA): ")
            try:
                data_nascimento = datetime.strptime(data_de_nascimento_str, "%d/%m/%Y")
                return data_nascimento
            except ValueError:
                print("Data inválida. Por favor, digite no formato DD/MM/AAAA.")

def criar_conta(nome_usuario, data_nascimento, cpf_usuario):
    novo_usuario = {
                "nome": nome_usuario,
                "data_nascimento": data_nascimento.strftime("%d/%m/%Y"),
                "cpf": cpf_usuario,
                "conta_corrente": False,
                "saldo": 0,
                "extrato": "",
                "numero_saques": 0,
                "limite_saques": 3
            }
    contas.append(novo_usuario)    
    global posicao_da_conta
    posicao_da_conta += 1
            
menu_cpf_inicial = ("""
--==ENTRA CONTA/NÃO FINALIZADO==--
[Digite seu CPF (apenas números)]

=> """)


menu_inicial = ("""
--==MENU BANCO==--
[1] Entrar na conta
[2] Criar conta
[3] Listar contas
--==============--
=> """)

menu_operacoes = ("""
 --==OPERAÇÕES==--
[1] Depositar
[2] Sacar
[3] Ver extrato
=> """)


while True:
    opcao = input(menu_inicial)

    match opcao:
        case "1":
            menu_cpf_usuario = input(menu_cpf_inicial)
            if tem_conta(menu_cpf_usuario):
                if tem_conta_corrente(menu_cpf_usuario):
                    
    

                    opcao_operacoes = input(menu_operacoes)

                    match opcao_operacoes:
                        case "1":
                            valor = float(input("Qual o valor que deseja depositar: "))
                            if valor > 0:
                                conta['cpf'] saldo_usuario += valor
                                print(f"O valor de R${valor} foi adicionado na sua conta")
                                extrato += f"Depósito de {valor}\n"
                            else:
                                print("Valor inválido")
                        case "2":
                            valor = float(input("Qual o valor que deseja sacar: "))
                            if 0 < valor <= saldo_usuario:
                                saldo_usuario -= valor
                                print(f"O valor de R${valor} foi creditado da sua conta")
                                extrato += f"Saque de R${valor}"
                            else:
                                print("Valor indisponível para saque.")
                        case "3":
                            print("--==EXTRATO==--")
                            print(extrato)
                        case _:
                            print("Opção inválida")
                else:
                    opcao_criar_conta_corrente = input("Deseja criar conta corrente [S/N]: ")
                    if opcao_criar_conta_corrente == "S" or opcao_criar_conta_corrente == "s":
                        for conta in contas:
                            if conta["cpf"] == menu_cpf_usuario:
                                numero_conta_corrente = 1000 + posicao_da_conta
                                conta_corrente = f"{agencia} {numero_conta_corrente}"
                                conta.update({"conta_corrente": True, "numero_conta_corrente": conta_corrente})
                                print("Conta corrente criada com sucesso.")
            else:   
                print("Usuário não cadastrado.")

        case "2":
                print("--==CRIAR CONTA==--")
                nome_usuario = input("Nome para cadastro: ")
                data_nascimento = solicitar_data_nascimento()
                cpf_usuario = int(input("Cpf para cadastro (apenas números): "))

                if any(conta['cpf'] == cpf_usuario for conta in contas):
                    print("CPF já cadastrado")
                else:
                    criar_conta(nome_usuario, data_nascimento, cpf_usuario)
                
        case "3":
                  for conta in contas:
                    print(f"Nome {conta['nome']}, Data de nascimento {conta['data_nascimento']}, CPF:{conta['cpf']}, Conta corrente: {'Sim' if conta["conta_corrente"] else "Não"} " )
        case _:
            print("Opção Inválida")
        
        
    
    





