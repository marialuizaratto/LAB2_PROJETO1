def cumprimento(texto):
    return f"Olá, {texto}"
print(cumprimento("Maria Luiza Ratto"))

import random

def sorteia_media():
    numeros = [random.randint(1, 100) for _ in range(7)]  
    media = sum(numeros) / len(numeros)
    return media

print("Média dos 7 números sorteados:", sorteia_media())
