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

def  h_index_linear(citacoes):
    h = 0
    for i in range(len(citacoes)):
        if citacoes[i] >= i + 1:
            h = i + 1
        else:
            break
    return h


def h_index_binaria_decrescente(citacoes):
    inicio = 0
    fim = len(citacoes) - 1
    h = 0

    while inicio <= fim:
        meio = (inicio + fim) // 2
        h = meio + 1
        if citacoes[meio] >= h:
            inicio = meio + 1
        else:
            fim = meio - 1
    return inicio


def two_sum_brute_force(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []