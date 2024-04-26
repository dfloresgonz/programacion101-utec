def pregunta_1(cadena: str) -> float:
  promedio = 0
  suma = 0
  for nota in cadena:
    suma += float(nota)
  promedio = suma / len(cadena)
  promedio = round(promedio, 2)
  return promedio

def pregunta_2(cadena: str, palabra: str) -> str:
  #resultado = None
  existe = True
  for p in palabra:
    if p.lower() not in cadena.lower():
      existe = False
      break
  return "Se puede formar la palabra" if existe else "No se puede formar la palabra"

def pregunta_3(numero: int) -> list:
  lista = []
  while True:
    if len(lista) != 0:
      if numero % 2 == 0:
        numero = numero / 2
      else:
        numero = (numero * 3) + 1

    lista.append(int(numero))
    if numero == 1:
      break
  return lista

def pregunta_4(frase: str, numero_rotaciones: int) -> str:
  idx = 0
  newidx = 0
  new_frase = [char for char in frase]
  for i in frase:
    if idx >= numero_rotaciones:
      newidx = idx - numero_rotaciones
    else:
      newidx = idx + (len(frase) - numero_rotaciones)

    new_frase[newidx] = i
    idx += 1
  solucion = ''.join(new_frase)
  return solucion