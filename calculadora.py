

def dividir(primer_numero: int, segundo_numero: int) -> int:
     
    
    cociente = 0
    while primer_numero >= segundo_numero:
        primer_numero -= segundo_numero
        cociente += 1
    return cociente

print(dividir(12, 3))
print("esperado:4")
print(dividir(30, 5))
print("esperado:6")
print(dividir(40, 8))
print("esperado:5")
print(dividir(25, 0))