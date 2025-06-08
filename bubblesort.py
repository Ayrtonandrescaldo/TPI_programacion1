def sort(array):
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

