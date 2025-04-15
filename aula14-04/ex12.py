#---------FOLHA DE PAGAMENTO----------#
#---------dados requisitados----------#
valorHora = float(input("Digite o valor da sua hora: "))
horasMes = int(input("Digite quantas horas trabalhadas por mes: "))

#---------variaveis----------#
salarioBruto = valorHora * horasMes
desconto5 = ((salarioBruto * 5) / 100)
desconto10 = ((salarioBruto * 10) / 100)
desconto20 = ((salarioBruto * 20) / 100)
inss = 110.00
fgts = 121.00

#---------salario bruto menor que 900 reais----------#
if salarioBruto <= 900:
    print(f"Salario bruto: ________________________R$ {salarioBruto}")
    print(f"(-)IR (5%): ___________________________R$ {desconto5}")
    print(f"(-)INSS (10%): ________________________R$ {inss}")
    print(f"FGTS (11%): ___________________________R$ {fgts}")
    print(f"Total de descontos: ___________________R$ {desconto5 + inss}")
    print(f"Lucro Líquido: ________________________R$ {salarioBruto - (desconto5 + inss)}")

#---------salario bruto menor que 1500 reais----------#
elif salarioBruto <= 1500:
    print(f"Salario bruto: ________________________R$ {salarioBruto}")
    print(f"(-)IR (5%): ___________________________R$ {desconto5}")
    print(f"(-)INSS (10%): ________________________R$ {inss}")
    print(f"FGTS (11%): ___________________________R$ {fgts}")
    print(f"Total de descontos: ___________________R$ {desconto5 + inss}")
    print(f"Lucro Líquido: ________________________R$ {salarioBruto - (desconto5 + inss)}")

#---------salario bruto menor que 2500 reais----------#
elif salarioBruto <= 2500:
    print(f"Salario bruto: ________________________R$ {salarioBruto}")
    print(f"(-)IR (5%): ___________________________R$ {desconto10}")
    print(f"(-)INSS (10%): ________________________R$ {inss}")
    print(f"FGTS (11%): ___________________________R$ {fgts}")
    print(f"Total de descontos: ___________________R$ {desconto10 + inss}")
    print(f"Lucro Líquido: ________________________R$ {salarioBruto - (desconto10 + inss)}")

#---------salario bruto acima de 2500 reais----------#
elif salarioBruto > 2500:
    print(f"Salario bruto: ________________________R$ {salarioBruto}")
    print(f"(-)IR (5%): ___________________________R$ {desconto20}")
    print(f"(-)INSS (10%): ________________________R$ {inss}")
    print(f"FGTS (11%): ___________________________R$ {fgts}")
    print(f"Total de descontos: ___________________R$ {desconto20 + inss}")
    print(f"Lucro Líquido: ________________________R$ {salarioBruto - (desconto20 + inss)}")