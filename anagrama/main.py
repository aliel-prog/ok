"""
Crea una funció que rebi dos strings i determini si són anagrames (contenen les mateixes lletres organitzades diferent),
ignorant els espais en blanc, símbols de puntuació ni majúscules o minúscules.
Exemple
Entrada: "tom marvolo riddle", "i am lord voldemort"
Sortida: True
"""
import  logica
import  interficie

if __name__ == "__main__":
    # 1. Pedir palabras (o usar datos de prueba)
    palabra1, palabra2 = interficie.pedir_palabras()
    
    # 2. Comprobar usando logica.py
    resultado = logica.son_anagramas(palabra1, palabra2)
    
    # 3. Mostrar el resultado usando interficie.py
    interficie.mostrar_resultado(resultado)
"""
No he tenido que utilizar el apartado de config.py 
porque no tengo ni reglas ni constantes que tengan cambiar algo antes de la ejecucion del programa,
dades.py no a hecho falta tampoco porque no hay ni listas ni diccionarios donde haya tenido que guardar algo.
""" 