def _limpiar_palabra(palabra):
    palabra = palabra.lower().strip()
    caracteres_a_quitar = [" ", ",", "."]
    for c in caracteres_a_quitar:
        palabra = palabra.replace(c, "")
    return palabra

def _tienen_mismo_len(palabra1, palabra2):
    return len(palabra1) == len(palabra2)

def _letter_in_word(palabra1, palabra2):
    for letter in palabra1:
        if letter in palabra2:
            palabra2 = palabra2.replace(letter, "", 1)
        else:
            return False
    return True

def son_anagramas(palabra1, palabra2):
    palabra1 = _limpiar_palabra(palabra1)
    palabra2 = _limpiar_palabra(palabra2)

    if _tienen_mismo_len(palabra1, palabra2):
        return _letter_in_word(palabra1, palabra2)
    
    return False
