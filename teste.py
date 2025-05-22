try:
    a = int(input("digite uma palavra"))

except ValueError: #erro do tipo valor 
    print("Digite apenas numeros")

except:
    print("Erro desconhecido")

finally:
    print("final do algoritmo")