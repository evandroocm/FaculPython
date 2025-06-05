# Crie uma função que receba dois números e retorne a soma deles.
def soma_numeros(num1, num2):
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    return num1 + num2

resultado = soma_numeros(0, 0)
print(f"A soma dos números é: {resultado}")