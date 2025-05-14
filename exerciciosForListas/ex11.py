prod = float(input("Preço do pão: "))

print("Panificadora Pão de Ontem - Tabela de Preços")
for i in range(1,51):
    print(f"{i} - R$ {i * prod:.2f}")