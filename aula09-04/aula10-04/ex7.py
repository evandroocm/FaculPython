num1 = int(input("Digite um numero: "))
num2 = int(input("Digite outro numero: "))
num3 = int(input("Digite outro numero: "))

maior = num1
menor = num1

if num2 > maior:
    maior = num2
if num3 > maior:
    maior = num3

if num2 < menor:
    menor = num2
if num3 < menor:
    menor = num3

print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")