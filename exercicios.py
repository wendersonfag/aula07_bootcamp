from etl import calcular_media, valor_acima_do_limite

#exercico 01
lista: list = [44,88,100,2]

media_resultado: float = calcular_media(lista)

print(media_resultado)


# exercio 02
lista_produto: list[dict] = [{"produto":"perfume","valor": 100},{"produto":"notebook","valor": 1000},{"produto":"controle","valor": 10},{"produto":"xbox","valor": 2000}]


produtos_limite: list[dict] = valor_acima_do_limite(lista_produto)

print(produtos_limite)
