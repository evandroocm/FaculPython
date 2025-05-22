clientes = {}
passagens = {}
avioes = {}
tripulacao = {}

while True:
    print("""
==== Sistema de Passagem Aérea ====
1. Cadastrar Cliente
2. Cadastrar Passagem
3. Cadastrar Avião
4. Cadastrar Tripulação
5. Relatórios
6. Sair
===================================
""")

    opcao = input('Escolha uma opção: ')

    if opcao == '1':
        try:
            cpf = int(input('Digite o CPF do cliente (apenas números): '))
            if cpf in clientes:
                print('Cliente já cadastrado!')
                continue
            nome = input('Nome: ')
            sobrenome = input('Sobrenome: ')
            idade = int(input('Idade: '))
            rg = int(input('RG (Apenas números): '))
            telefone = int(input('Telefone (Apenas números): '))
            endereco = input('Endereço: ')

            clientes[cpf] = {
                'nome': nome,
                'sobrenome': sobrenome,
                'idade': idade,
                'rg': rg,
                'cpf': cpf,
                'telefone': telefone,
                'endereco': endereco
            }

            print(f'Cliente {cpf} cadastrado com sucesso!')
        except ValueError:
            print('Erro! Digite apenas números nos campos numéricos.')

    elif opcao == '2':
        try:
            numero = input('Numero da passagem: ')
            if numero in passagens:
                print('Passagem já cadastrada!')
                continue
            cpf = int(input('CPF do cliente: '))
            if cpf not in clientes:
                print('Cliente não cadastrado!')
                continue
            aviao = input('Código do avião: ')
            if aviao not in avioes:
                print('Avião não cadastrado!')
                continue
            trip = input('Código da tripulação: ')
            if trip not in tripulacao:
                print('Tripulação não cadastrada!')
                continue
            origem = input('Origem: ')
            destino = input('Destino: ')
            data = input('Data do voo: ')
            horario = input('Horário do voo: ')

            passagens[numero] = {
                'cpf': cpf,
                'aviao': aviao,
                'tripulacao': trip,
                'origem': origem,
                'destino': destino,
                'data': data,
                'horario': horario
            }

            print(f'Passagem {numero} cadastrada com sucesso!')
        except ValueError:
            print('Digite apenas numeros')

    elif opcao == '3':
        codigo = input('Código do avião: ')
        if codigo in avioes:
            print('Avião já cadastrado!')
            continue
        modelo = input('Modelo: ')
        try:
            capacidade = int(input('Capacidade (apenas números): '))
        except ValueError:
            print('Capacidade deve ser um número.')
            continue

        avioes[codigo] = {
            'modelo': modelo,
            'capacidade': capacidade
        }
        print(f'Avião {codigo} cadastrado com sucesso!')

    elif opcao == '4':
        codigo = input('Código da tripulação: ')
        if codigo in tripulacao:
            print('Tripulação já cadastrada!')
            continue
        piloto = input('Nome do piloto: ')
        copiloto = input('Nome do copiloto: ')
        comissarios = input('Comissários (separados por vírgula): ').split(',')
        tripulacao[codigo] = {
            'piloto': piloto,
            'copiloto': copiloto,
            'comissarios': [c.strip() for c in comissarios]
        }
        print(f'Tripulação {codigo} cadastrada com sucesso!')

    elif opcao == '5':
        print("\nRelatório de Clientes: ")
        for cpf, dados in clientes.items():
            print(f"{cpf}: {dados['nome']} {dados['sobrenome']}")

        print("\nRelatório de Passagens: ")
        for num, dados in passagens.items():
            nome_cliente = clientes.get(dados['cpf'], {}).get('nome', 'Desconhecido')
            print(f"{num}: Cliente: {nome_cliente} - Origem: {dados['origem']} - Destino: {dados['destino']} - Data: {dados['data']}")

        print("\nRelatório de Aviões: ")
        for codigo, dados in avioes.items():
            print(f"{codigo}: Modelo: {dados['modelo']} - Capacidade: {dados['capacidade']}")

        print("\nRelatório de Tripulação: ")
        for codigo, dados in tripulacao.items():
            print(f"{codigo}: Piloto: {dados['piloto']} - Copiloto: {dados['copiloto']} - Comissários: {', '.join(dados['comissarios'])}")

    elif opcao == '6':
        print('Saindo do sistema...')
        break

    else:
        print('Opção inválida!')