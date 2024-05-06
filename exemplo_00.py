def soma(valor_1_para_somar: float, valor_2_para_somar: float) -> float:
    """
    uma função simple de soma de valores do tipo gloat que retorna float
    """
    resultado_da_somar: float = valor_1_para_somar + valor_2_para_somar
    return resultado_da_somar



valor_1 = 4

valor_2 = 6

valor_4 = 50

valor_5 = 30

valor_3 = soma(valor_1_para_somar= valor_1, valor_2_para_somar= valor_2)

valor_6 = soma(valor_4, valor_5)

print(valor_3)

print(valor_6)

#pode passar um parametro padrão
def soma2(valor_1_para_somar: float, valor_2_para_somar: float = 10) -> float:
    """
    uma função simple de soma de valores do tipo gloat que retorna float
    """
    resultado_da_somar: float = valor_1_para_somar + valor_2_para_somar
    return resultado_da_somar



valor_7 = soma2(valor_5)



print(valor_7)