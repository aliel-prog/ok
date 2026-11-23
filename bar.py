def avaluar_estat_bar(nom_bar: str , te_tapa:bool , preu_cervesa: float , nota_clients: float , es_artesana: bool = False) -> string 

if te_tapa = True and preu_cervesa <= 2.50 and nota_clients >= 4.5: 
    res = "DESTACAT_TOP"
elif te_tapa = True and nota_clients >= 4.0:  
    res = "MOLT_RECOMANABLE"
elif te_tapa = False and es_artesana = True and preu_cervesa <= 3.00: 
    res "BON_PREU"
else 
    res = "ESTANDAR"
return "[DIAGNOSTIC] Bar:" +nom_bar+ " Estat: " + res

test_1 = avaluar_estat_bar("El raco de la Tapa", True, 2.20, 4.8)
test
