# A empresa Umbrella Corporation está desenvolvendo seu sistema de cadastro de pacientes, e a 
# primeira fase do projeto consiste um desenvolver um algoritmo que capte os dados de cadastro.

# Tal cadastro solicitará os seguintes dados: (nome, cpf, rg, data de nascimento, sexo, peso,
# tipo sanguíneo, renda, endereço, telefone, cidade e estado)

# Após capturar todos os dados, imprimir em forma de relatório.

print("\n=============== Umbrella Corporation ================")
print("===================== Cadastro ======================")

nomeCompleto = input("Digite seu nome completo: ")
cpf = input("Digite seu CPF: ") #ate colocaria int, mas pesquisei e vi que geralmente utilizam como str, por conta dos zeros a esquerda!
rg = input("Digite seu RG: ") #mesma coisa do cpf
dataNascimento = input("Digite sua data de nascimento (DD/MM/AAAA): ")
sexo = input("Digite seu sexo: ")
peso = float(input("Digite seu peso: "))
tipoSanguineo = input("Digite seu tipo sanguineo: ")
renda = float(input("Digite sua renda: "))
endereco = input("Digite seu endereço: ")
telefone = input("Digite seu telefone: ")
cidade = input("Digite sua cidade: ")
estado = input("Digite seu estado: ")

print("\n=============== Umbrella Corporation ================")
print("================ Relatório Cadastro =================")
print(f"\nNome: {nomeCompleto}")
print(f"\nCPF: {cpf}")
print(f"\nRG: {rg}")
print(f"\nData Nascimento: {dataNascimento}")
print(f"\nSexo: {sexo}")
print(f"\nPeso: {peso}:.2f")
print(f"\nTipo Sanguineo: {tipoSanguineo}")
print(f"\nRenda: {renda}")
print(f"\nEndereço: {endereco}")
print(f"\nTelefone: {telefone}")
print(f"\nCidade: {cidade}")
print(f"\nEstado: {estado}")