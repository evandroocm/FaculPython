def calcular_pagamento(qntd_horas, valor_total):
    horas = float(qntd_horas)
    taxa = float(valor_total)
    if horas <= 40:
        salario = horas * taxa
    else:
        h_excd = horas - 40
        salario = 40 * taxa + (h_excd * (1.5 * taxa))
    print(f"Valor do salario bruto R$ {salario} reais")

calcular_pagamento(40, 100)