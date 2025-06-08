import time 
import random
import bogosort
import bubblesort
import quicksort

def calculateExecutionTime(function, array):
    # Ejecutamos el calculo de tiempo 3 iteraciones
    executionTimes = []
    for i in range(3):
        # Iniciamos el tiempo de ejecucion
        startTime = time.perf_counter()
        # Ejecutamos el algoritmo de ordenamiento
        function(array)
        # Finalizamos el tiempo de ejecucion
        endTime = time.perf_counter()
        # Agregamos el tiempo de ejecucion a la lista
        executionTimes.append(endTime - startTime)
    
    # Calculamos el promedio de tiempo de ejecucion
    averageExecutionTime = sum(executionTimes) / 3

    return {"#":len(array), "executionTimes":executionTimes, "averageExecutionTime":averageExecutionTime}
    

# Ejecutamos los algoritmos de ordenamiento para una lista de 10 elementos
array=[i for i in range(10)] 
random.shuffle(array)
print(calculateExecutionTime(quicksort.sort, array))
print(calculateExecutionTime(bubblesort.sort, array))
print(calculateExecutionTime(bogosort.sort, array))


# Ejecutamos los algoritmos de ordenamiento para una lista de 100 elementos
array = [i for i in range(100)]
random.shuffle(array)
print(calculateExecutionTime(quicksort.sort, array))
print(calculateExecutionTime(bubblesort.sort, array))
print(calculateExecutionTime(bogosort.sort, array))
