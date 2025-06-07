#Crie uma função que receba uma lista de nomes e retorne apenas os nomes com mais de 5 letras.
def nomes_maiores_que_cinco(nomes):
    return [nome for nome in nomes if len(nome) > 5]

nomes = ['Mateus', 'Pedro', 'Paulo', 'Kiko', 'Santiago']