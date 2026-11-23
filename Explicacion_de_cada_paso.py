    """
 mirando cada posición i de la palabra una por una 
 (desde la posición 0 que es la "r" hasta la posición 6 que es la última "a").
 Por cada letra que analizas, creas una lista temporal distancias = [] para apuntar a qué distancia están todas las "a" de esa posición.
 Con for j in range(len(rattata)): vuelves a recorrer toda la palabra usando otro índice j para encontrar 
 dónde aparece la letra buscada (if rattata[j] == a:).
    """

    """
        Cuando encuentra una "a", calcula la distancia entre tu posición actual (i) y la posición de esa "a" (j) usando abs(i - j). 
        La función abs() asegura que el número siempre sea positivo.
        Guarda esa distancia en la lista temporal distancias.
        """