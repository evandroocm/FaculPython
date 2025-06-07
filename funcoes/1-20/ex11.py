#Crie uma função que receba um número e retorne uma lista com todos os divisores dele.
def divisores(numero):
    lista_divisores = []
    for i in range(1, numero + 1):
        if numero % i == 0:
            lista_divisores.append(i)
    return lista_divisores

numero = int(input('Digite um número: '))
print(f'Os divisores do número {numero} são: {divisores(numero)}')