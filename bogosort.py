import random

def bogosort(array):
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


# Ejemplo de uso
numbers = [3,5,12,421,3]
sortedNumbers = bogosort(numbers)
print("Sorted numbers:", sortedNumbers) 