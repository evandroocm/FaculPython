# Listas
clientes = []
cliente = []

# Loop principal
while True:
    print("\nCadastro do cliente:")
    while True:
        nome = input("Nome: ").strip().upper()
        if nome == "":
            break
        cliente.append(nome)

        cpf = input("CPF: ").strip().upper()
        cliente.append(cpf)

        rg = input("RG: ").strip().upper()
        cliente.append(rg)

        telefone = input("Telefone: ").strip().upper()
        cliente.append(telefone)

        numAgencia = input("Numero da Agencia: ").strip().upper()
        cliente.append(numAgencia)

        numConta = input("Numero da conta: ").strip().upper()
        cliente.append(numConta)

        saldoInicial = float(input("Saldo inicial: "))
        cliente.append(saldoInicial)

        clientes.append(cliente.copy())
        cliente.clear()

        continuar = input("Deseja cadastrar outro cliente? (S/N): ").strip().upper()
        if continuar != "S":
            break

    # Loop menu
    while True:
        print("\nEscolha a operação: ")
        print("1 - Ver saldo")
        print("2 - Depositar")
        print("3 - Sacar")
        print("4 - Voltar para o cadastro de cliente")

        opcao = input("Digite a opção desejada: ").strip()

        if opcao == "1":
            cpf = input("Digite o CPF do cliente: ").strip().upper()
            encontrado = False
            for cliente in clientes:
                if cliente[1] == cpf:
                    print(f"Seu saldo é: {cliente[6]:.2f}")
                    encontrado = True
                    break
            if not encontrado:
                print("Cliente não encontrado.")

        elif opcao == "2":
            cpf = input("Digite o CPF do cliente: ").strip().upper()
            encontrado = False
            for cliente in clientes:
                if cliente[1] == cpf:
                    valorDeposito = float(input("Digite o valor a depositar: "))
                    cliente[6] += valorDeposito
                    print(f"Depósito realizado. Novo saldo: {cliente[6]:.2f}")
                    encontrado = True
                    break
            if not encontrado:
                print("Cliente não encontrado.")

        elif opcao == "3":
            cpf = input("Digite o CPF do cliente: ").strip().upper()
            encontrado = False
            for cliente in clientes:
                if cliente[1] == cpf:
                    valorSaque = float(input("Digite o valor a sacar: "))
                    if cliente[6] >= valorSaque:
                        cliente[6] -= valorSaque
                        print(f"Saque realizado. Novo saldo: {cliente[6]:.2f}")
                    else:
                        print("Saldo insuficiente.")
                    encontrado = True
                    break
            if not encontrado:
                print("Cliente não encontrado.")

        elif opcao == "4":
            print("Voltando para o cadastro de cliente...\n")
            break

        else:
            print("Opção inválida. Tente novamente.")