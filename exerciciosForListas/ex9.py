candidato1 = 12435
candidato2 = 45678
candidato3 = 76524
x = 0
y = 0
z = 0

eleitores = int(input("Digite o numero total de eleitores: "))

for i in range(eleitores):
    voto = int(input("Digite seu voto para vereador: "))
    if voto != 12435 and voto != 45678 and voto != 76524:
        print("Por favor, digite outro número!")
        break
    
    if voto == candidato1:
        x += 1
    elif voto == candidato2:
        y += 1
    elif voto == candidato3:
        z += 1
    else:
        print("Número invalido, digite novamente")

if x > y and x > z:
    print("Candidato 1 é o campeão")
elif y > x and y > z:
    print("Candidato 2 é o campeão")
elif z > x and z > y:
    print("Candidato 3 é o campeão")

print(f"\nNumero de votos: ")
print(f"Candidato 1: {x} votos")
print(f"Candidato 2: {y} votos")
print(f"Candidato 3: {z} votos")