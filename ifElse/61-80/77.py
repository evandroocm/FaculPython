#77 - Verifique se um número é múltiplo de 3 ou 5, mas não de 7.
number = 15
if (number % 3 == 0 or number % 5 == 0) and number % 7 != 0:
    print("Múltiplo de 3 ou 5, mas não de 7")
else:
    print("Não atende aos critérios")