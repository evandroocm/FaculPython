salarioAtual = float(input("Digite o valor do seu salario atual: "))

reajuste15 = salarioAtual * 1.15
reajuste10 = salarioAtual * 1.10
reajuste5 = salarioAtual * 1.05

if (salarioAtual < 500):
    print(f"Salário reajustado: {reajuste15 :.2f}")
elif (salarioAtual >= 500 and salarioAtual < 1000):
    print(f"Salário reajustado: {reajuste10 :.2f}")
elif (salarioAtual > 1000):
    print(f"Salário reajustado: {reajuste5 :.2f}")