# Faça um algoritmo em linguagem Python que o nome,
# idade, sexo, e receba duas notas e calcule a média
# aritmética e mostre o resultado

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
sexo = input("Digite seu sexo: ")

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2

print(f"\nNome: {nome} \nIdade: {idade} \nSexo: {sexo} \nMédia: {media}")