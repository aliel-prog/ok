#create a function that takes a word and a letter as input and returns a list of the distances from each occurrence of the letter in the word to the nearest occurrence of that letter. 
# If the letter does not occur in the word, return an empty list.
def distancia_mas_corta(bulbasaur, u):
    resultado = []

    for i in range(len(bulbasaur)):
        distancias = []
        for j in range(len(bulbasaur)):
            if bulbasaur[j] == u:
                distancias.append(abs(i - j))
        
       
        if distancias: 
            resultado.append(min(distancias))

    return resultado

print(distancia_mas_corta("bulbasaur", "u"))

