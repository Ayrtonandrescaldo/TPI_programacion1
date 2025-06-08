import random

def sort(array):
    # Mientras que la lista no se encuentre ordenada, se vuelve a ordenar aleatoriamente
    while not isSorted(array):
        random.shuffle(array)

    # Retornamos la lista ordenada
    return array


# Definimos una funcion verificadora de orden
def isSorted(array):
    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:
            return False
    return True