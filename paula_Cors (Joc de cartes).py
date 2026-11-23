'''
Cosas que se deben hacer
1. Identificar el palo
2. Filtrar las cartas validas (solo se deben de quedar con las cartas del mismo palo)
3. Buscar la mas alta (2, 10, j, q, k, a)
4. Devolver el texto exacto, dar la baraja de la carta ganadora tal cual entro. RESPETANDO LAS MAYUSCULAS.

Explicacion del juego:
El juego trata sobre un juego de cartas, trevol, corazones, diamantes y picas. 4 personas sacan 1 carta, el primero q saca una carta 3c
si nadie saca una carta mayor de la misma mano por ejemplo 6c gana el primero.

'''

mano = ['10C', 'JC','AC', 'QC']

def iniciacion_juego(mano):
    palo_obligatorio = mano[0][-1] 
    
    orden_valores = ["2" , "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

# Identificar la carta mas alta
    carta_ganadora = mano[0]

    for carta in mano:
        palo_carta = carta[-1]
        valor_carta = carta[:-1]
        # El [:-1] es para cortar el texto y quita la parte final, ejemplo (JC) pues nos quedariamos con J

# Compara el palo oblifatorio con el que es ahora
        if palo_carta == palo_obligatorio:
            if orden_valores.index(valor_carta) > orden_valores.index(carta_ganadora):
                carta_ganadora = carta
    return carta_ganadora

juego = iniciacion_juego(mano)

print(f"Esta es la carta ganadora {carta_ganadora}")

    
    
