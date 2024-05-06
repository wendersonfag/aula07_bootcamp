lista: list = [44,88,100,2]

def calcular_media(lista_numero: list) -> float:
    media = sum(lista_numero) / len(lista)
    return media



media_resultado: float = calcular_media(lista)

print(media_resultado)