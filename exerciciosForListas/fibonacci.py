n = int(input("Digite a quantidade de termos: "))
 
if n > 0:
    a = 1
    b = 1
 
    print("Numeros:")
    for i in range(n):
        print(a, end=" ")
        proximo = a + b
        a = b
        b = proximo
else:
    print("Digite um número positivo.")