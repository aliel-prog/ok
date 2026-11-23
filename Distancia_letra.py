#Creo la funcion que voy a usar
def distancia_letra (rattata, a):
    resultado = []
    """
     mirando cada posición i de la palabra una por una 
     (desde la posición 0 que es la "r" hasta la posición 6 que es la última "a").
     Por cada letra que analizas, creas una lista temporal distancias = [] para apuntar a qué distancia están todas las "a" de esa posición.
     Con for j in range(len(rattata)): vuelves a recorrer toda la palabra usando otro índice j para encontrar 
     dónde aparece la letra buscada (if rattata[j] == a:).
    """
    for i in range(len(rattata)):
        distancias = []
        for j in range(len(rattata)):
            if rattata[j] == a:
                distancias.append(abs(i - j))
        """
        Cuando encuentra una "a", calcula la distancia entre tu posición actual (i) y la posición de esa "a" (j) usando abs(i - j). 
        La función abs() asegura que el número siempre sea positivo.
        Guarda esa distancia en la lista temporal distancias.
        """
    if distancias:
        resultado.append(min(distancias))
 
    #devolver y imprimir el resultado del calculo de las distancias.

    return resultado
print(distancia_letra("rattata", "a"))

