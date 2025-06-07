
import time

def quicksort(array):
    # Condicion de corte de recursividad para evitar que se ejecute infinitamente
    if len(array) <= 1:
        return array

    # Tomamos el primer elemento de la lista como elemento de referencia
    target = array[0]

    # Definimos las listas vacias que contendran los elementos menores y mayores al elemento de referencia
    lessThanTarget = []
    greaterThanTarget = []

    # Recorremos la lista y comparamos cada elemento con el elemento de referencia
    for i in array[1:]:
        if i <= target:
            lessThanTarget.append(i)
        else:
            greaterThanTarget.append(i)

    # Invocamos la funcion recursivamente para ordenar el resto de elementos comprendidos en las listas de menores y mayores
    return quicksort(lessThanTarget) + [target] + quicksort(greaterThanTarget)

# Iniciamos el contador de tiempo
startTime = time.perf_counter()

# Ejemplo de uso
numbers = [3,5,12,3,2,451,5,1]
sortedNumbers = quicksort(numbers)
print("Sorted numbers:", sortedNumbers) 

# Calculamos y mostramos el tiempo de ejecucion
endTime = time.perf_counter()

print("Execution time: ", endTime - startTime)