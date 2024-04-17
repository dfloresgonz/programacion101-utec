from math import sqrt
def pregunta_1(arista:  float) -> float:
    volumen = 1/4 * (15 + 7 * sqrt(5)) * pow(arista, 3)
    volumen = round(volumen, 3)
    return volumen

def pregunta_2(lado1: float, lado2: float, lado3: float, lado4:float) ->float: 
    s = (lado1+lado2+lado3+lado4)/2
    k = sqrt( (s - lado1) * (s - lado2) * (s - lado3) * (s - lado4) )
    k = round(k, 3)
    return k

def pregunta_3(numero : int)->str:
    cant=0
    dig1=numero//100
    rest = numero % 100
    dig2=rest // 10
    dig3=numero%10
    print(dig1,dig2,dig3)
    if dig1==dig2==dig3:
        cant = 3
    elif dig1==dig2 and dig3!=dig1:
        cant = 2
    elif dig1 == dig3 and dig2 != dig1:
        cant = 2
    elif dig2 == dig3 and dig2 != dig1:
        cant = 2
    return cant

def pregunta_4( rango :  int) -> str: 
    nivel=""
    if rango <= 69:
        nivel = "Deficiente"
    elif rango >= 70 and rango <= 79:
        nivel = "Inferior"
    elif rango >= 80 and rango <= 89:
        nivel = "Abajo del promedio"
    elif rango >= 90 and rango <= 109:
        nivel = "Promedio"
    elif rango >= 110 and rango <= 119:
        nivel = "Arriba del promedio"
    elif rango >= 120 and rango <= 129:
        nivel = "Superior"
    elif rango >= 130:
        nivel = "Muy superior"
    return nivel
