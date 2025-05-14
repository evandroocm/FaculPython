num = int(input("Digite um número inteiro para calcular o fatorial: "))
fatorial = 1
 
print(f"{num}! =", end=" ")
 
for i in range(num, 0, -1):
    fatorial *= i
    if i != 1:
        print(f"{i}.", end="")
    else:
        print(f"{i}", end="")
 
print(f" = {fatorial}")