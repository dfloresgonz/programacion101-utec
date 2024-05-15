from typing import List

# Pregunta 1.1 (Diego Flores G.)


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

# Pregunta 1.2 (Diego Flores G.)


def rotar_lista(lista: List[int], n: int) -> List[int]:
  """
  Rotar una lista de enteros n veces.
  """
  return lista[-n:] + lista[:-n]


lista = [1, 2, 3, 4, 5, 6, 7]
# n = 3
n = -2
print(rotar_lista(lista, n))
