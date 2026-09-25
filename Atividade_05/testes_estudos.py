def ordenar_sem_metodos(array):
    array_novo = [0] * len(array)

    for elemento_atual in array:
        contador = 0
        for outro_elemento in array:
            if outro_elemento < elemento_atual:
                contador += 1
        array_novo[contador] = elemento_atual
    return array_novo

lista_teste = [10, 15, 2, 3, 5, 12, 1, 7, 8, 9]
print(ordenar_sem_metodos(lista_teste))

def bubble_sort(array):
    n = len(array)

    for i in range(n):
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]: #compara os vizinhos
                array[j], array[j + 1] = array[j + 1], array[j] #troca

lista = [10, 15, 2, 3, 5, 12, 1, 7, 8, 9]
bubble_sort(lista)
print(lista)