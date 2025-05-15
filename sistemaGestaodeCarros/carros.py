carros = {}

def menu():
    print("""\n==== Sistema de Gestão de Carros ====
1. Adicionar Carro
2. Listar Todos os Carros
3. Buscar Carro por Nome
4. Atualizar Informações do Carro
5. Remover Carro
6. Sair
===================================\n""")

def adicionar_carro():
    nome = input('Digite o nome do carro: ')
    if nome in carros:
        print('Carro já cadastrado!')
        return
    carros[nome] = {
        'km': int(input('Digite a quilometragem: ')),
        'ano': int(input('Digite o ano: ')),
        'cor': input('Digite a cor: '),
        'modelo': input('Digite o modelo: '),
        'potencia': input('Digite a potência: '),
        'combustivel': input('Digite o tipo de combustível: '),
        'cambio': input('Digite o tipo de câmbio: ')
    }
    print(f'Carro {nome} adicionado com sucesso!')

def listar_carros():
    if not carros:
        print('Nenhum carro cadastrado.')
    else:
        for nome, dados in carros.items():
            print(f'Nome: {nome} - Dados: {dados}')

def buscar_carro():
    nome = input('Digite o nome do carro para buscar: ')
    if nome in carros:
        print(f'Dados do {nome}: {carros[nome]}')
    else:
        print('Carro não encontrado.')

def remover_carro():
    nome = input('Digite o nome do carro para remover: ')
    if nome in carros:
        del carros[nome]
        print(f'Carro {nome} removido com sucesso!')
    else:
        print('Carro não encontrado.')

def main():
    while True:
        menu()
        opcao = input('Escolha uma opção: ')
        if opcao == '1':
            adicionar_carro()
        elif opcao == '2':
            listar_carros()
        elif opcao == '3':
            buscar_carro()
        elif opcao == '4':
            print('Em desenvolvimento...')
        elif opcao == '5':
            remover_carro()
        elif opcao == '6':
            print('Saindo do sistema...')
            break
        else:
            print('Opção inválida!')

main()