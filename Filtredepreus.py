def analizador_precios_bebidas(precio_maximo_presupuesto) -> str:
    precios_aceptables = []

    for precio in precios:
        if precio <= precio_maximo_presupuesto:
            precios-aceptables,append (precio)

    if len(precios_aceptables) == 0:
        precio_media = 0
    else:
        med = len(precios_aceptables)
        precio_media = round(sum(precios_aceptables) / med, 2)
    return (
        "precios_aceptables": precios_aceptables,
        "precio_media": precio_media
        "quedan_opciones": len(precios_aceptables) > 0

print(analizador_precios_bebidas([2.5, 3.0, 4.2, 1.8], 3.0))
print(analizador_precios_bebidas([5.0, 6.5], 3.0))
print(analizador_precios_bebidas([], 3.0))
