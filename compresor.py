"""
Escriu una funció que agafi un string de caràcters repetits de forma consecutiva i 
retorni una versió "comprimida" indicant la lletra seguida del número de vegades que es repeteix. 
Si només surt una vegada, no fa falta afegir el número).
Ejemplo:
Entrada: "aaabcccccaaa"
Sortida: "a3bc5a3"
"""
def comprimir_string(s):
    if not s:
        return ""
    
    comprimido = []
    letra_actual = s[0]
    contador = 1

    for i in range(1, len(s)):
        if s[i] == letra_actual:
            contador += 1
        else:
            if contador == 1:
                comprimido.append(letra_actual)
            else:
                comprimido.append(f"{letra_actual}{contador}")
            letra_actual = s[i]
            contador = 1

    # Afegir l'última seqüència
    if contador == 1:
        comprimido.append(letra_actual)
    else:
        comprimido.append(f"{letra_actual}{contador}")

    return "".join(comprimido)

print(comprimir_string("aaabcccccaaa"))
print(comprimir_string("aabbbccccdddeee"))
print(comprimir_string("abcde"))
print(comprimir_string("assfijjjwiiiwfvvvngvh"))

