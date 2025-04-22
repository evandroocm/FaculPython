#71 - Verifique se um número é maior que 50, mas não é múltiplo de 5.
number = 52
if number > 50 and number % 5 != 0:
    print("Maior que 50 e não múltiplo de 5")
else:
    print("Não atende os dois critérios")