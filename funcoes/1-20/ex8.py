#Crie uma função que inverta uma string.
def inverter_string(texto):
    return texto[::-1]

string_input = input("Digite uma string para inverter: ")

string_invertida = inverter_string(string_input)

print(f"A string invertida é: {string_invertida}")