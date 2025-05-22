#dicionarios, armazenar dados
clientes = {}
passagens = {}
avioes = {}
tripulacao = {}

#menu principal
def menu():
    print("""\n==== Sistema de Passagem Aérea ====
1. Cadastrar Cliente
2. Cadastrar Passagem
3. Cadastrar Avião
4. Cadastrar Tripulação
5. Relatórios
6. Sair
===================================\n""")

def cadastrar_cliente():
    while True:
        try:
            cpf = int(input('Digite o CPF do cliente (apenas números): '))
            break
        except ValueError:
            print("Digite apenas números.")

    if cpf in clientes:
        print('Cliente já cadastrado!')
        return

    nome = input('Nome: ')
    sobrenome = input('Sobrenome: ')

    while True:
        try:
            idade = int(input('Idade: '))
            break
        except ValueError:
            print("Digite um número válido para a idade.")

    while True:
        try:
            rg = int(input('RG (Apenas números): '))
            break
        except ValueError:
            print("Digite apenas números para o RG.")

    while True:
        try:
            telefone = int(input('Telefone (Apenas números): '))
            break
        except ValueError:
            print("Digite apenas números para o telefone.")

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

    print(f'Cliente {cpf} adicionado com sucesso!')

def cadastrar_passagem():
    while True:
        try:
            passagem = int(input('Digite o numero da Passagem: '))
            break
        except ValueError:
            print("Digite apenas números.")

    if passagem in clientes:
        print('Cliente já cadastrado!')
        return

    nome = input('Nome: ')
    sobrenome = input('Sobrenome: ')

    while True:
        try:
            idade = int(input('Idade: '))
            break
        except ValueError:
            print("Digite um número válido para a idade.")

    while True:
        try:
            rg = int(input('RG (Apenas números): '))
            break
        except ValueError:
            print("Digite apenas números para o RG.")

    while True:
        try:
            telefone = int(input('Telefone (Apenas números): '))
            break
        except ValueError:
            print("Digite apenas números para o telefone.")

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

    print(f'Cliente {cpf} adicionado com sucesso!')

    # if not clientes:
    #     print('Nenhum cliente cadastrado.')
    # else:
    #     for nome, dados in clientes.items():
    #         print(f'Nome: {nome} - Dados: {dados}')

# def buscar_carro():
#     nome = input('Digite o nome do carro para buscar: ')
#     if nome in clientes:
#         print(f'Dados do {nome}: {clientes[nome]}')
#     else:
#         print('Carro não encontrado.')

# def remover_carro():
#     nome = input('Digite o nome do carro para remover: ')
#     if nome in clientes:
#         del clientes[nome]
#         print(f'Carro {nome} removido com sucesso!')
#     else:
#         print('Carro não encontrado.')

def relatorios():
    print("""\n==== Relatórios ====
        1. Relatório Clientes
        2. Relatório Passagens
        3. Relatório Aviões
        4. Relatório Tripulação
        5. Sair
        ===================================\n""")

def main():
    while True:
        menu()
        opcao = input('Escolha uma opção: ')
        if opcao == '1':
            cadastrar_cliente()
        elif opcao == '2':
            cadastrar_passagem()
        elif opcao == '3':
            cadastrar_aviao()
        elif opcao == '4':
            cadastrar_tripulacao()
        elif opcao == '5':
            relatorios()
            while True:
                opcao = print('Escolha uma opção: ')
                if opcao == '1':
                    print("bla")
        elif opcao == '6':
            print('Saindo do sistema...')
            break
        else:
            print('Opção inválida!')

main()