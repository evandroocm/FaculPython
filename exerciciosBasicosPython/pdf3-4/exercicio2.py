nome = (input("Digite o nome do produto: "))
qtde = int(input("Digite a quantidade de produtos: "))
valor = float(input("Digite o valor unitário: "))
desc = float(input("Digite o valor do desconto: "))

total = float(valor - (valor*desc / 100))

print("\nNome: ", nome)
print("Quantidade: ", qtde)
print("Valor Unitário: R$ ", valor)
print("Desconto: ", desc, "%")
print("Valor Total: R$ ", total)