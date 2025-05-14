pares = 0
impares = 0

for i in range(10):
    num = int(input(f"Digite o {i + 1}º numero: "))
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f"Quantidade de numeros pares: {pares}")
print(f"Quantidade de numeros impares: {impares}")