import time

def bubblesort(array):
    # Definimos número de elementos de la lista
    lenght = len(array)

    # Recorremos la lista
    for i in range(lenght):
        # En cada iteracion los elementos mayores que el elemento actual se mueve hacia el final de la lista
        for j in range(0, lenght - i - 1):
            # Se compara el elemento actual con el siguiente, intercambiandolo si es necesario
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

    return array

# Iniciamos el contador de tiempo
startTime = time.perf_counter()

# Ejemplo de uso
numbers = [3,5,12,3,2,451,5,1,23,5,73,21,4,12,1]
sortedNumbers = bubblesort(numbers)
print("Sorted numbers:", sortedNumbers)

# Calculamos y mostramos el tiempo de ejecucion
endTime = time.perf_counter()

print("Execution time: ", endTime - startTime)
