import random

def pedir_numero():
    return float(input("Introduce un número: "))

numeros = []
for i in range(3):
    print(f"Número {i+1}:")
    num = pedir_numero()
    numeros.append(num)

suma = sum(numeros)
print(f"La suma de los 3 números es: {suma}")