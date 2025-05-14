qntd = int(input("Quantas temperaturas? "))
infos = []
 
for i in range(qntd):
    temp = float(input(f"Informe a temperatura {i + 1}: "))
    mes = input(f"Informe o mês da temperatura {i + 1}: ")
    ano = input(f"Informe o ano da temperatura {i + 1}: ")
    infos.append((temp, mes, ano))
 
menor = infos[0]
maior = infos[0]
soma = 0
 
for temp, mes, ano in infos:
    if temp < menor[0]:
        menor = (temp, mes, ano)
    if temp > maior[0]:
        maior = (temp, mes, ano)
    soma += temp

media = soma / qntd
 
print(f"Menor: {menor[0]}°C em {menor[1]}/{menor[2]}")
print(f"Maior: {maior[0]}°C em {maior[1]}/{maior[2]}")
print(f"Média: {media:.2f}°C")