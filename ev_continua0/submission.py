from math import sqrt

def pregunta_1(arista:  float) -> float:
  volumen = 1/4 * (15 + 7 * sqrt(5)) * arista**3
  r = round(volumen, 3)
  return r

def pregunta_2(lado1: float, lado2: float, lado3: float, lado4:float) ->float: 
  s = (lado1 + lado2 + lado3 + lado4)/2
  k = sqrt((s - lado1) * (s - lado2) * (s - lado3) * (s - lado4))
  r = round(k, 3)
  return r

def pregunta_3(numero : int)->str:
  resp=""
  dig1=numero//100
  rest = numero % 100
  dig2=rest // 10
  dig3=numero%10
  if dig1==dig2==dig3:
    resp="Tiene tres digitos iguales"
  elif dig1==dig2 and dig3!=dig1:
    resp="Tiene solo dos digitos iguales"
  elif dig1 == dig3 and dig2 != dig1:
    resp="Tiene solo dos digitos iguales"
  elif dig2 == dig3 and dig2 != dig1:
    resp="Tiene solo dos digitos iguales"
  return resp

def pregunta_4( rango :  int) -> str: 
  nivel=""
  if rango <= 69:
    nivel = "Deficiente"
  elif rango >= 70 and rango < 80:
    nivel = "Inferior"
  elif rango >= 80 and rango < 90:
    nivel = "Abajo del Promedio"
  elif rango >= 90 and rango < 110:
    nivel = "Promedio"
  elif rango >= 110 and rango < 120:
    nivel = "Arriba del Promedio"
  elif rango >= 120 and rango < 130:
    nivel = "Superior"
  else:
    nivel = "Muy Superior"
  return nivel
