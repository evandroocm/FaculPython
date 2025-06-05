#Crie uma função que calcule o fatorial de um número (sem usar recursão).
def fatorial(n):
    if n < 0:
        return "Fatorial não definido para números negativos."
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

numero = int(input("Digite um número para calcular o fatorial: "))
print(f"O fatorial de {numero} é: {fatorial(numero)}")