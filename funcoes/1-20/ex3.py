#Escreva uma função que calcule o quadrado de um número.
def quadrado(numero):
    numero = float(input("Digite um número: "))
    return numero ** 2

resultado = quadrado(0)
print(f"O quadrado do número é: {resultado}")