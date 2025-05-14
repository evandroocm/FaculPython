print("============= Acidentes de Transito em 1999 =============")
numCidades = int(input("Digite o numero de cidades: "))
cidades = []

for i in range(numCidades):
    cod = int(input("Digite o código da cidade: "))
    numVeiculos = int(input("Digite o número de veículos de passeio (em 1999): "))
    numAcidentes = int(input("Digite o número de acidentes de trânsito com vítimas (em 1999): "))
    cidades.append((cod, numVeiculos, numAcidentes))

menor = cidades[0]
maior = cidades[0]
soma = 0
somaMenos2000 = 0
totalCid = 0
 
for cod, numVeiculos, numAcidentes in cidades:
    if numAcidentes < menor[2]:
        menor = (cod, numVeiculos, numAcidentes)
    if numAcidentes > maior[2]:
        maior = (cod, numVeiculos, numAcidentes)
    soma += numAcidentes
    
    if numVeiculos < 2000:
        somaMenos2000 += numAcidentes
        totalCid += 1

media = soma / numCidades

if totalCid > 0:
    mediaMenos2000 = somaMenos2000 / totalCid
else:
    mediaMenos2000 = 0

print(f"\nA cidade de código {maior[0]} teve o maior número de acidentes.")
print(f"A cidade de código {menor[0]} teve o menor número de acidentes.")
print(f"A média de acidentes das {numCidades} cidades é: {media:.2f}")
print(f"A média de acidentes nas cidades com menos de 2.000 veículos de passeio é: {mediaMenos2000:.2f}")