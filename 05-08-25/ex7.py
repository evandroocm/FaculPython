#-----VARIAVEIS-----#
valor = 0
soma = 0
menor = float("inf")
maior = float("-inf")

for i in range(5):
    print("Digite o", i + 1, "º valor")
    valor = int(input())
    soma += valor

    if(valor < menor):
        menor = valor
    elif(valor > maior):
        maior = valor


print(f"A soma é: {soma}")
print(f"O maior é: {maior}")
print(f"O menor é: {menor}")