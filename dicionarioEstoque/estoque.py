estoque = {
    "chaves": 16,
    "garrafa": 25,
    "celular": 54,
    "mouse": 345,
    "tenis": 22,
    "pulseira": 231,
    "cadeado": 28,
    "boia": 24,
    "geleia": 52,
    "mesa": 25,
    "caixa de som": 70
}

produto = input("Digite o nome do produto: ")

if produto in estoque:
    print(f"{produto} = {estoque[produto]} unidades.")
else:
    print(f"Produto não está disponivel.")