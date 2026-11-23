def pedir_palabras():
    palabra1 = input("Introdueix la primera paraula o frase: ")
    palabra2 = input("Introdueix la segona paraula o frase: ")
    return palabra1, palabra2

def mostrar_resultado(es_anagrama):
    if es_anagrama:
        print("Són anagrames!")
    else:
        print("No són anagrames.")
