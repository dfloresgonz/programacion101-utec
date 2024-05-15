from typing import List, Dict

#################### 1.1 #####################


def combinar_y_ordenar(lista1: List[int], lista2: List[int]) -> List[int]:
  """
  Combinar dos listas de enteros, eliminar duplicados y ordenar el resultado.
  """
  combined = lista1 + lista2
  unique = set(combined)
  return sorted(unique)


lista1 = [3, 1, 4, 1, 5]
lista2 = [9, 2, 6, 5, 3, 5]
# print(combinar_y_ordenar(lista1, lista2))

#################### 1.2 #####################


def rotar_lista(lista: List[int], n: int) -> List[int]:
  """
  Rotar una lista de enteros n veces.
  """
  return lista[-n:] + lista[:-n]


lista = [1, 2, 3, 4, 5, 6, 7]
# n = 3
n = -2
# print(rotar_lista(lista, n))


#################### 1.3 #####################

def combinanciones_sumatorias(lista: List[int], target: int) -> List[List[int]]:
  dp = [[] for _ in range(target + 1)]
  dp[0] = [[]]

  for num in lista:
    for i in range(num, target + 1):
      for combination in dp[i - num]:
        dp[i].append(combination + [num])
  return dp[target]

# print(combinanciones_sumatorias(lista=[2, 3, 6, 7], target=7))

#################### 2.1 #####################


def suma_matrices(matriz1: List[List[int]], matriz2: List[List[int]]) -> List[List[int]]:
  if len(matriz1) != len(matriz2) or len(matriz1[0]) != len(matriz2[0]):
    raise ValueError("Las dimensiones de las matrices no coinciden")
  resultado = []
  for i in range(len(matriz1)):
    fila_resultado = []
    for j in range(len(matriz1[0])):
      fila_resultado.append(matriz1[i][j] + matriz2[i][j])
    resultado.append(fila_resultado)
  return resultado


matriz1 = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]

matriz2 = [[9, 8, 7],
           [6, 5, 4],
           [3, 2, 1]]

# print(suma_matrices(matriz1, matriz2))

#################### 2.2 #####################


def producto_matrices(matriz_1: List[List[int]], matriz_2: List[List[int]]) -> List[List[int]]:
  if len(matriz_2[0]) != len(matriz_1):
    raise ValueError("Las matrices no son compatibles para la multiplicación.")
  matriz_r = [[0 for _ in range(len(matriz_2[0]))]
              for _ in range(len(matriz_1))]
  for i in range(len(matriz_1)):
    for j in range(len(matriz_2[0])):
      for k in range(len(matriz_2)):
        matriz_r[i][j] += matriz_1[i][k] * matriz_2[k][j]

  return (matriz_r)


matriz_1 = [[1, 2], [3, 4]]
matriz_2 = [[5, 6], [7, 8]]
# print(producto_matrices(matriz_1, matriz_2))

#################### 2.3 #####################


def camino_minimo(matriz: List[List[int]]) -> int:
  m = len(matriz)
  n = len(matriz[0])

  matriz_suma = [[0 for _ in range(n)] for _ in range(m)]
  matriz_suma[0][0] = matriz[0][0]
  for i in range(1, n):
    matriz_suma[0][i] = matriz_suma[0][i - 1] + matriz[0][i]
  for j in range(1, m):
    matriz_suma[j][0] = matriz_suma[j - 1][0] + matriz[j][0]
  for i in range(1, m):
    for j in range(1, n):
      matriz_suma[i][j] = min(matriz_suma[i - 1][j],
                              matriz_suma[i][j - 1]) + matriz[i][j]

  return matriz_suma[m - 1][n - 1]


matriz = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
# print(camino_minimo(matriz))
#################### 3.1 #####################


def contar_ocurrencias(lista: list):
  dict = {}
  unique_list = list(set(lista))
  for i in unique_list:
    dict[i] = lista.count(i)
  return dict


lista = ['a', 'b', 'a', 'c', 'b', 'a', 'd']
# print(contar_ocurrencias(lista))

#################### 3.2 #####################


def combinar_diccionarios(
        dic1: dict[any, int],
        dic2: dict[any, int]) -> dict:
  union_dict = set(dic1) | set(dic2)
  nuevo_diccionario = {clave: dic1.get(
      clave, 0) + dic2.get(clave, 0) for clave in union_dict}

  return nuevo_diccionario


dic1 = {'a': 1, 'b': 2, 'c': 3}
dic2 = {'c': 4, 'b': 3, 'd': 5}

# print(combinar_diccionarios(dic1, dic2))

#################### 3.3 #####################


def frecuencia_palabras(documentos: List[str]) -> Dict[str, int]:
  # Crear un diccionario vacío para almacenar la frecuencia de palabras
  frecuencia = {}

  # Recorrer cada documento en la lista de documentos
  for documento in documentos:
      # Dividir el documento en palabras individuales
    palabras = documento.split()
    # Recorrer cada palabra en el documento y actualizar su frecuencia en el diccionario
    for palabra in palabras:
      if palabra in frecuencia:
        frecuencia[palabra] += 1
      else:
        frecuencia[palabra] = 1

  return frecuencia


# Ejemplo de uso:
documentos = [
    "este es el primer documento",
    "el segundo documento es mas largo",
    "este es el tercer documento"
]
# print(frecuencia_palabras(documentos))


# INTEGRANTES - GRUPO 7

# Enrique Arauco, Javierth Lisnerth
# Flores Gonzales, Diego Rafael
# Palacios Chilo, Jorge Luis
# Peinado Rodriguez, Enrique Alexis
# Vilela Gutierrez, Diego Orlando
