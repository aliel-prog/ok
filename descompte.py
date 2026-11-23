def aplicar_descompte_soci(soci):
    quota_anual = 120.0
    total = quota_anual
    if soci["anys_soci"] > 3:
          total = quota_anual * 0.85
    return total

nou_soci 0 {"nom": "Pol", "anys_soci": 1}
quota = aplicar_descompte_soci(nou_soci)
print(f"Quota a pagar: {quota}$")

