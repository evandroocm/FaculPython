#Escreva uma função que receba uma palavra e retorne True se ela for um palíndromo.
def eh_palindromo(palavra):
    palavra = palavra.lower()  # Ignora diferenças entre maiúsculas e minúsculas
    return palavra == palavra[::-1]  # Compara a palavra com sua reversa
if __name__ == "__main__":
    palavra = "arara"
    resultado = eh_palindromo(palavra)
    print(f"A palavra '{palavra}' é um palíndromo? {resultado}")
    
    palavra2 = "python"
    resultado2 = eh_palindromo(palavra2)
    print(f"A palavra '{palavra2}' é um palíndromo? {resultado2}")

    palavra