def cumprimento(texto):
    return f"Olá, {texto}"
print(cumprimento("Maria Luiza Ratto"))

import random

import random

def sorteia_media():
    numeros = [random.randint(1, 100) for _ in range(7)]
    media = sum(numeros) / len(numeros)
    return numeros, media

numeros_sorteados, media = sorteia_media()
print("Números sorteados:", numeros_sorteados)
print(f"Média dos 7 números sorteados: {media:.2f}")


