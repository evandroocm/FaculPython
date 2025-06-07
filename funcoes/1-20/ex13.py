#Crie uma função que receba uma string e retorne a mesma string sem espaços.
def string_sem_espacos(texto):
    return texto.replace(" ", "")

texto = input('Digite uma texto: ')
print(f'String sem espaços: {string_sem_espacos(texto)}')