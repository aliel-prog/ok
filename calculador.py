def calcular_preu_oferta(preu_base: float,es_soci: bool,dia_setmana: str = "Dilluns") -> float: preu_oferta = 0.0
if preu_base <= 0:
    preu_base = 0.0
elif es_soci == True and dia_setmana == "Dijous": 
    preu_oferta = preu_base * 0.8
elif dia_setmana =="Dijous":
    preu_oferta = preu_base * 0.95
elif es_soci == True: 
    preu_oferta = preu_base * 0.85

return round(preu_oferta, 2)

precio_final = calcular_preu_oferta(0,False)
print(precio_final)
