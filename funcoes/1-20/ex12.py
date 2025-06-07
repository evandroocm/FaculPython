#Crie uma função que converta graus Celsius para Fahrenheit.
def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

celcius = float(input('Digite a temperatura em celsius: '))
print(f'A temperatura em Fahrenheit é: {celsius_para_fahrenheit(celcius)} graus')