def calcular_tiquet(factura, taxa=1.02):
    factura["total"] = factura["total"] * taxa
    return factura
comanda_real = {"id": 894, "client": "Marta", "total": 100.0}
calcular_tiquet(comanda_real)
calcular_tiquet(comanda_real)


def calcular_tiquet(factura: dict, taxa: float = 1.02) 
    factura_neta = factura.copy()

    factura_neta["total"] = round(factura)