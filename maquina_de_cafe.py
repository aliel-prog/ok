
'''
1.mostrar menu
  -1.expresso(1.00$)
  -2.cafe con leche (1.50$)
  -3. chocolate (1.20$)
2. Leer selección del usuario
3. Solicitar inserción de dinero hasta que dinero >= precio
4. Calcular cambio (si dinero > precio)
5. Activar componentes:
  -calentar agua
  -dossificar café / leche / azucar
  -servir en vaso
  6.mostrar mensaje de "disfrute su cafe!" y devolver cambio
'''
def maquina_cafe():


def bebidas(menu: dict, precio: int) -> int:
    bebidas={
      1:mensaje:"Expresso",precio:1.00,
      2:mensaje:"Café con leche",precio:1.50,
      3:mensaje:"Chocolate",precio:1.20,
    }
    return bebidas
    
def solicitar_dinero(bebidas, selection):
    precio = bebidas.get(selection, {}).get('precio')
money = 0
falta_pagar = precio
print(f"te queda por pagar: {falta_pagar}")
while money < precio:
    money += float(input("Inserte dinero: "))
    falta_pagar = precio - money
    
  return money
def calcular_cambio(selection,money):

def activar_componentes():

def finalizar(selection,exchange):

  maquina_cafe()