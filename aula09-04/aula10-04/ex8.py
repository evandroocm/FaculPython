prod1 = float(input("Digite o preço do primeiro produto: "))
prod2 = float(input("Digite o preço do segundo produto: "))
prod3 = float(input("Digite o preço do terceiro produto: "))

if prod1 < prod2 and prod1 < prod3:
    print("Compre o produto 1")
elif prod2 < prod1 and prod2 < prod3:
    print("Compre o produto 2")
else:
    print("Compre o produto 3")