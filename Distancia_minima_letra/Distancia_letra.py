def distancia_letra(rattata, a):
    resultado = []

    for i in range(len(rattata)):
        distancias = []
        for j in range(len(rattata)):
            if rattata[j] == a:
                distancias.append(abs(i - j))
        if distancias:
            resultado.append(min(distancias))

    return resultado

print(distancia_letra("rattata", "a"))
