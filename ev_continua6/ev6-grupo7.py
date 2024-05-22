# grupo 7
import numpy as np

# 1.1


def reemplazar_multiplos():
  arr = np.arange(1, 101)
  mult_3 = (arr % 3 == 0)
  mult_5 = (arr % 5 == 0)

  arr[mult_3] = -1
  arr[mult_5] = -1
  return arr


print(reemplazar_multiplos())

# 1.2


def elementos_impares(vector):
  vector_impares = vector[1::2]
  return vector_impares


vector = np.arange(1, 21)
print(elementos_impares(vector))

# 1.3


def operacion_broadcasting(vector, numero: int, operacion: str):
  if operacion == 'suma':
    vector[:] += numero
  elif operacion == 'resta':
    vector[:] -= numero
  elif operacion == 'multiplicacion':
    vector[:] *= numero
  elif operacion == 'division':
    vector = vector / numero
  return vector


v1 = np.array([1, 2, 3])
print(operacion_broadcasting(v1, 2, 'division'))

# 1.4


def filtrar_pares_negativos(vector):
  vector[vector % 2 == 0] = -vector[vector % 2 == 0]
  return vector


vector = np.arange(1, 10)  # 1 2 3 4 5 6 7 8 9
print(filtrar_pares_negativos(vector))

# 1.5


def intercalar_vectores(n):
  vector1 = np.arange(n)
  print(vector1)
  vector2 = np.random.rand(n)
  print(vector2)
  # Creamos un nuevo vector de longitud 2n para almacenar los elementos intercalados
  intercalado = np.empty(2*n)
  intercalado[0::2] = vector1
  intercalado[1::2] = vector2
  return intercalado


n = 5
resultado = intercalar_vectores(n)
print(resultado)

# 1.6


def reemplazar_elementos(n, indices, valores):
  vector = np.arange(n)
  # Verifica que la longitud de indices y valores sea la misma
  if len(indices) != len(valores):
    raise ValueError(
        "La longitud de los índices y los valores debe ser la misma.")
  # Verifica que los índices estén dentro del rango válido
  if any(idx < 0 or idx >= n for idx in indices):
    raise IndexError("Uno o más índices están fuera del rango válido.")
  # Reemplaza los elementos en los índices especificados
  for idx, val in zip(indices, valores):
    vector[idx] = val
  return vector


n = 10
indices = [2, 4, 6]
valores = [100, 200, 300]
resultado = reemplazar_elementos(n, indices, valores)
print(resultado)

# 1.7


def permutar_y_rebanar(n: int, k: int) -> np.ndarray:
  arr = np.arange(0, n)
  np.random.shuffle(arr)
  reb_arr = arr[:k]
  return reb_arr


print(permutar_y_rebanar(10, 4))

# 1.8


def operaciones_avanzadas(v1, v2):
    # Verificación que los vectores de entrada tengan la misma longitud
  if len(v1) != len(v2):
    raise ValueError("Los vectores deben tener la misma longitud")

  # Aplicando la función no lineal (seno) al primer vector v1:
  # Se aplica el sen() en radiaciones a cada elemento y se almacena
  v1_sin = np.sin(v1)

  # Concatenando (uniendo) los dos vectores resultantes en un solo vector:
  vector_concatenado = np.concatenate((v1_sin, v2))

  # Calculando el producto punto (producto escalar) del vector concatenado consigo mismo
  producto_punto = np.dot(vector_concatenado, vector_concatenado)

  # Retornar el resultado del producto punto
  return producto_punto


# Ejemplo de uso
v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])
resultado = operaciones_avanzadas(v1, v2)
print("Resultado del Producto Punto del Vector Concatenado consigo Mismo:", resultado)

# 1.9


def operaciones_estadisticas(datos):
  # Calcula la media
  media = np.mean(datos)

  # Calcula la mediana
  mediana = np.median(datos)

  # Calcula la desviación estándar
  desviacion_estandar = np.std(datos)

  # Retorna los tres valores como una tupla
  return (media, mediana, desviacion_estandar)


# Ejemplo de uso
datos = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
                 12, 13, 14, 15, 16, 17, 18, 19, 20])
estadisticas = operaciones_estadisticas(datos)
print("Media:", estadisticas[0])
print("Mediana:", estadisticas[1])
print("Desviacion Estandar:", estadisticas[2])
