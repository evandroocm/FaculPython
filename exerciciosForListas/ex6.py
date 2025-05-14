valor = 0
soma = 0
cont = 0

for i in range(5):
    print("Digite o", i + 1, "º valor")
    valor = int(input())
    soma += valor
    cont += 1

print(f"A soma é: {soma}")
print(f"A média é: {soma / cont}")