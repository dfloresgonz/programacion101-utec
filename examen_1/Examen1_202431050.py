
def pregunta_1(temp_exterior_celcius: int, hora: int) -> str:
  salida: str = ""
  if temp_exterior_celcius < 5:
    salida = "Encender"
  elif temp_exterior_celcius > 20:
    salida = "Apagar"
  elif (temp_exterior_celcius >= 5 and temp_exterior_celcius <= 20) and (hora >= 18 or hora <= 6):
    salida = "Encender"
  return salida

# test cases
# print(pregunta_1(2, 12))
# print(pregunta_1(22, 17))
# print(pregunta_1(10, 20))

def pregunta_2(cant_genes: int, cant_genes_year: str) -> str:
  # declaring variables
  is_incrementing: bool = False
  is_decrementing: bool = False
  last_value: int = 0
  max_index: int = 0
  idx: int = 0
  # useful variables for logic
  int_array = [int(num) for num in cant_genes_year.split()]
  max_index = int_array.index(max(int_array))
  for i in int_array:
    if i > last_value and idx <= max_index and idx != 0:
      is_incrementing = True
    elif i < last_value and idx > max_index and idx != 0:
      is_decrementing = True
    idx += 1
    last_value = i
  result = is_incrementing and is_decrementing
  return "Estable" if result == True else "Inestable"

# print(pregunta_2(9, "1 2 3 4 5 4 3 2 1"))
# print(pregunta_2(6, "1 3 2 4 5 6"))
# print(pregunta_2(5, "10 9 8 7 6"))

def pregunta_3(frecuencias: str) -> str:
  last_value: int = 0
  idx: int = 0
  diff: int = 0
  res: bool = True
  for i in [int(num) for num in frecuencias.split()]:
    print(i)
    if idx > 0:
      if idx == 1:
        diff = i - last_value
      if (i - last_value) != diff:
        res = False
    last_value = i
    idx += 1
  return "Armonica" if res == True else "No armonica"

# print(pregunta_3("200 400 600 800"))
# print(pregunta_3("300 450 600 900"))
# print(pregunta_3("128 256 384 512"))

# 300 - (20)
# 100 - x
def hayAnomalia(idx: int, ventas_array, umbral: int) -> bool:
  if idx < 7:
    return False
  else:
    print((idx-7),idx)
    last_ventas = ventas_array[(idx-7):idx]
    print(last_ventas)
    last_ventas = sum(last_ventas)
    print("sum:", last_ventas)
    average = last_ventas / 7
    print("average:", average)
    porcentaje = ( ( average - ventas_array[idx]) * 100) / average
    print("porcentaje:", porcentaje, "venta:", ventas_array[idx])
    if porcentaje >= umbral:
      print("anomalia {} {} {} {}".format(porcentaje, umbral, average, ventas_array[idx]))
      return True
    else:
      return False

def pregunta_4(ventas: str, umbral: int) -> str:
  ventas_array = [int(num) for num in ventas.split(",")]
  cant = 0
  idx = 0
  anomalia_total: bool = False
  for venta in ventas_array:
    if hayAnomalia(idx, ventas_array, umbral):
      cant += 1
    else:
      cant = 0
    idx += 1
    if cant > 14:
      anomalia_total = True
      break
    else:
      anomalia_total = False
  if anomalia_total == True:
    return "Anomalia detectada"
  else:
    return "Sin anomalia"

print(pregunta_4("100,200,180,190,200,210,205,198,165,160,155,150,145,140,135,130,125,120,115,110,105,100,95,90,85,80,75,70,65,60", 10))
# print(pregunta_4("100,102,101,103,105,104,106,108,110,109,107,105,103,101,100,102,104,106,108,110,112,114,116,118,120,122,124,126,128,130", 5))