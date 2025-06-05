#Escreva uma função que verifique se um número é par.
def num_par(n):
    n = int(input("Digite um número: "))
    if n % 2 == 0:
        print("O número digitado é par.")
    else:
        print("O número digitado é ímpar.")

num_par('')