
def sort(array):
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
    return sort(lessThanTarget) + [target] + sort(greaterThanTarget)
