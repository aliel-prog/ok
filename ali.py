def calcular_cuota_bizum(total_despesa: float, num_persones: int = 3, concepte: str = "Despesa") -> str: """calcula la divisio exacta de despeses entre companys de pis"""
  quota = round (total_despesa / num_persones, 2)
return  "concepte: " + concepte + ",Total: " + str(total_despesa) + ",per cap: " +str(quota)
                         
print(calcula_quota_bizum(84.00, 3, "Factura luz"))
print(calcula_quota_bizum(45.00, 3, "Intenet"))
print(calcula_quota_bizum (60.00, 2, "cena"))
