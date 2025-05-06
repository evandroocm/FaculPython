#Listas
clientes = []
cliente = []

# Cadastro do cliente
print("Cadastro do cliente: ")
while True:
    nome = input("Nome: ").upper()
    if nome == "":
        break
    cliente.append(nome)

    cpf = input("CPF: ").upper()
    cliente.append(cpf)

    rg = input("RG: ").upper()
    cliente.append(rg)

    telefone = input("Telefone: ").upper()
    cliente.append(telefone)

    numAgencia = input("Numero da Agencia: ").upper()
    cliente.append(numAgencia)

    numConta = input("Numero da conta: ").upper()
    cliente.append(numConta)

    saldoInicial = float(input("Saldo inicial: "))
    cliente.append(saldoInicial)

    #Cópia do cliente na lista de clientes
    clientes.append(cliente.copy())
    #Limpa a lista de cliente
    cliente.clear()

# Loop principal
opcao = ""
while opcao != "4":
    print("\nEscolha a operação: ")
    print("1 - Ver saldo")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Sair")

    opcao = input("Digite a opção desejada: ").upper()

    if opcao == "1":
        cpf = input("Digite o CPF do cliente: ").upper()
        encontrado = False
        for cliente in clientes:
            if cliente[1] == cpf:
                print(f"Seu saldo é: {cliente[6]}")
                encontrado = True
                break
        if not encontrado:
            print("Cliente não encontrado.")
        
    elif opcao == "2":
        cpf = input("Digite o CPF do cliente: ").upper()
        encontrado = False
        for cliente in clientes:
            if cliente[1] == cpf:
                valorDeposito = float(input("Digite o valor a depositar: "))
                cliente[6] += valorDeposito
                print(f"Seu novo saldo é: {cliente[6]}")
                encontrado = True
                break
        if not encontrado:
            print("Cliente não encontrado.")

    elif opcao == "3":
        cpf = input("Digite o CPF do cliente: ").upper()
        encontrado = False
        for cliente in clientes:
            if cliente[1] == cpf:
                valorSaque = float(input("Digite o valor a sacar: "))
                if cliente[6] >= valorSaque:
                    cliente[6] -= valorSaque
                    print(f"Seu novo saldo é: {cliente[6]}")
                else:
                    print("Saldo insuficiente.")
                encontrado = True
                break
        if not encontrado:
            print("Cliente não encontrado.")
    
    elif opcao == "4": 
        