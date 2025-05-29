nomes = []
idades = []
sexos = []
cpfs = []
enderecos = []
cidades = []
estados = []

while True:
    print("Menu:")
    print("1 - Cadastrar pessoa")
    print("2 - Consultar dados")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ");

    if opcao == '1':
        while True:
            nome = input("Nome: ").strip()
            try:
                idade = int(input("Idade: "))
            except ValueError:
                print("Erro. Digite novamente...")
                continue
            sexo = input("Sexo (M/F): ").strip().upper()
            cpf = input("CPF: ").strip()
            endereco = input("Endereço: ").strip()
            cidade = input("Cidade: ").strip()
            estado = input("Estado: ").strip().upper()

            nomes.append(nome)
            idades.append(idade)
            sexos.append(sexo)
            cpfs.append(cpf)
            enderecos.append(endereco)
            cidades.append(cidade)
            estados.append(estado)

            print("Cadastro realizado com sucesso!");

            continuar = input("Deseja cadastrar outra pessoa? (S/N): ").strip().upper()
            if continuar != 'S':
                break

    elif opcao == '2':
        if len(nomes) == 0:
            print("Nenhum cadastro encontrado.")
        else:
            for i in range(len(nomes)):
                print(f"{i + 1} - Nome: {nomes[i]}, Idade: {idades[i]}, Sexo: {sexos[i]}, CPF: {cpfs[i]}, "
                      f"Endereço: {enderecos[i]}, Cidade: {cidades[i]}, Estado: {estados[i]}")
            print('-' * 111)

            try:
                consulta = int(input("Digite o número do cadastro que deseja consultar (0 para voltar): "))
                if consulta == 0:
                    continue
                elif 1 <= consulta <= len(nomes):
                    i = consulta - 1
                    print(f"Nome: {nomes[i]}, Idade: {idades[i]}, Sexo: {sexos[i]}, CPF: {cpfs[i]}, "
                          f"Endereço: {enderecos[i]}, Cidade: {cidades[i]}, Estado: {estados[i]}")
                else:
                    print("Cadastro não encontrado.")
            except ValueError:
                print("Erro. Digite novamente...")

    elif opcao == '3':
        with open("cadastro.txt", "w") as arquivo:
            for i in range(len(nomes)):
                arquivo.write(f"Nome: {nomes[i]}, Idade: {idades[i]}, Sexo:{sexos[i]}, "
                              f"Endereço: {enderecos[i]}, Cidade: {cidades[i]}, Estado: {estados[i]}\n")
                arquivo.write('-' * 111 + '\n')
        print("Programa finalizado.")
        break

    else:
        print("Erro. Tente novamente.")