#-----VARIAVEIS-----#
valor = 0
soma = 0
maior = float("-inf")
menor = float("inf")

for i in range(5):
    print("Digite o", i + 1, "º valor")
    valor = int(input())
    soma += valor

    if(valor > maior):
        maior = valor
    elif(valor < menor):
        menor = valor


print(f"A soma é: {soma}")
print(f"O maior é: {maior}")
print(f"O menor é: {menor}")