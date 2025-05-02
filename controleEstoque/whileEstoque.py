# Dicionário com produtos e estoques
produtos = {
    10: ["Caderno", 0],
    20: ["Caneta", 0],
    30: ["Lápis", 0],
    40: ["Borracha", 0],
    50: ["Régua", 0]
}

# Cadastro inicial
print("Cadastro do estoque inicial: ")
for codigo in produtos:
    nome = produtos[codigo][0]
    quantidade = int(input(f"Digite o estoque inicial de {nome}: "))
    produtos[codigo][1] = quantidade

# Loop principal
opcao = ""
while opcao != "X":
    print("\nEscolha a operação: ")
    print("E - Entrada no estoque")
    print("S - Saída no estoque")
    print("R - Relatório")
    print("X - Sair")
    
    opcao = input("Digite a opção desejada: ").upper()

    if opcao == "E":
        cod = int(input("Digite o código do produto: "))
        if cod in produtos:
            qtd = int(input("Digite a quantidade a entrar no estoque: "))
            produtos[cod][1] += qtd
            print("Entrada realizada com sucesso!")
        else:
            print("Código inválido!")

    elif opcao == "S":
        cod = int(input("Digite o código do produto: "))
        if cod in produtos:
            qtd = int(input("Digite a quantidade a sair do estoque: "))
            if produtos[cod][1] >= qtd:
                produtos[cod][1] -= qtd
                print("Saída realizada com sucesso!")
            else:
                print("Estoque insuficiente!")
        else:
            print("Código inválido!")

    elif opcao == "R":
        print("\nRelatório de Estoque:")
        for cod in produtos:
            nome = produtos[cod][0]
            qtd = produtos[cod][1]
            print(f"{cod} - {nome}: {qtd} unidades")

    elif opcao == "X":
        print("Programa encerrado.")
    else:
        print("Opção inválida. Tente novamente.")