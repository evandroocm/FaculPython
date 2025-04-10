#Crie uma lista e substitua seus elementos por seus valores absolutos com abs().
lista = [-10, 5, -3, 8, -7, 0, 12, -1]

lista = [abs(num) for num in lista]

print(lista)