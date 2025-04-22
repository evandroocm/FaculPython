#56 - Verifique se um número é positivo e múltiplo de 3, mas não de 5.
number = 9
if number > 0 and number % 3 == 0 and number % 5 != 0:
    print("Positivo, múltiplo de 3 e não de 5")
else:
    print("Não atende aos critérios")