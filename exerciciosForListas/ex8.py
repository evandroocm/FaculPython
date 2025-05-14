n = int(input("Digite a quantidade de pessoas: "))
idades = []

for i in range(n):
    idade = int(input("Digite sua idade: "))
    idades.append(idade)

media = sum(idades) / n

if(media > 0 and media <= 25):
    print("\nTurma jovem.")
elif(media > 26 and media <= 60):
    print("\nTurma adulta.")
else:
    print("\nTurma idosa.")

print(f"A média é: {media}")