salarioAtual = float(input("Digite o valor do seu salario atual: "))

reajuste1 = ((salarioAtual * 22.51) / 100)
reajuste2 = ((salarioAtual * 15.39) / 100)
reajuste3 = ((salarioAtual * 10.97) / 100)
reajuste4 = ((salarioAtual * 5.19) / 100)

if (salarioAtual < 280.55):
    print(f"Salário antes do reajuste: {salarioAtual}\nPercentual de aumento: {((reajuste1 * 100) / salarioAtual)}\nValor do aumento: {reajuste1}\nSalário reajustado: {(reajuste1 + salarioAtual):.2f}")  
elif (salarioAtual >= 280.56 and salarioAtual < 709.72):
    print(f"Salário antes do reajuste: {salarioAtual}\nPercentual de aumento: {((reajuste2 * 100) / salarioAtual)}\nValor do aumento: {reajuste2}\nSalário reajustado: {(reajuste2 + salarioAtual):.2f}")
elif (salarioAtual >= 709.73 and salarioAtual < 1501.33):
    print(f"Salário antes do reajuste: {salarioAtual}\nPercentual de aumento: {((reajuste3 * 100) / salarioAtual)}\nValor do aumento: {reajuste3}\nSalário reajustado: {(reajuste3 + salarioAtual):.2f}")
elif (salarioAtual >= 1501.34):
    print(f"Salário antes do reajuste: {salarioAtual}\nPercentual de aumento: {((reajuste4 * 100) / salarioAtual)}\nValor do aumento: {reajuste4}\nSalário reajustado: {(reajuste4 + salarioAtual):.2f}")