def distancia_letra(palabra, letra):
    resultado = []

    for i in range(len(palabra)):
        distancias = []
        for j in range(len(palabra)):
            if palabra[j] == letra:
                distancias.append(abs(i - j))
        
       
        if distancias: 
            resultado.append(min(distancias))

    return resultado

print(distancia_letra("bulbasaur", "u"))
print(distancia_letra("abuela", "a"))
print(distancia_letra("tranvia", "a"))
print(distancia_letra("bebida", "i"))
"""
Ahora hay que volver a hacerlo, pero esta vez sin usar la funcion range. 
En su lugar, se puede usar un bucle while para iterar sobre los índices de la cadena bulbasaur. 
"""
def distancia_minima_letra(palabra, letra):
    distancias = []
    i = 0
    while i < len(palabra):
        if palabra[i] == letra:
            distancias.append(i)
        i += 1
    return distancias
        i += 1
    return distancias
print(distancia_minima_letra("abuela", "a"))
"""
nose hacerlo sin el range y con while porque el while no me deja iterar sobre los indices de la cadena, nose como hacerlo.
"""