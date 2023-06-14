def custom_max(n1: int, n2: int):
    """Dado dos numeros de entrada retorna el maximo de ambos

    Args:
        n1 (int): Primer numero a comparar
        n2 (int): Segundo numero a comparar

    Returns:
        int : Mayor de ambos
    """
    if n2 > n1:
        return n2
    elif n1 > n2:
        return n1
    elif n1 == n2:
        raise Exception("Los valores no pueden ser iguales")
    raise Exception("Algo salio mal")

print(custom_max(4, 4))

def max_de_tres(n1: int, n2: int, n3:int):
    n = custom_max(n1, n2)
    m = custom_max(n, n3)
    return m
    