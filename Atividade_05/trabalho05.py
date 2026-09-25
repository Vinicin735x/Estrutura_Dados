def quicksort(arr):
    """
    Função principal que inicia o QuickSort.
    Não exige passar índices, apenas o array.
    """
    _quicksort(arr, 0, len(arr) - 1)  # Chama a função recursiva passando os índices corretos.

def _quicksort(arr, left, right):
    """
    Função recursiva que implementa o QuickSort.
    Divide o array em partes menores ao redor do pivô.
    """
    if left < right:  # Caso base: quando a subarray tem pelo menos 2 elementos.
        pi = partition(arr, left, right)  # Particiona o array e obtém o índice do pivô.

        # Chamada recursiva para a subarray à esquerda do pivô.
        _quicksort(arr, left, pi - 1)

        # Chamada recursiva para a subarray à direita do pivô.
        _quicksort(arr, pi + 1, right)

def partition(arr, left, right):
    """
    Função de particionamento: organiza o array para o QuickSort.
    Coloca o pivô em sua posição correta e garante:
        elementos <= pivô ficam à esquerda dele
        elementos > pivô ficam à direita dele
    """
    pivot = arr[right]  # Escolhe o último elemento como pivô.

    i = left - 1  # Ponteiro para a posição de troca: começa antes da subarray.

    for j in range(left, right):  # Percorre todos os elementos do subarray (exceto o pivô).
        if arr[j] <= pivot:  # Se o elemento atual for menor ou igual ao pivô...
            i += 1  # Avança o ponteiro de troca.
            arr[i], arr[j] = arr[j], arr[i]  # Troca o elemento atual com o elemento na posição de troca.

    # Após o loop, coloca o pivô na posição correta (entre os menores e os maiores).
    arr[i + 1], arr[right] = arr[right], arr[i + 1]

    return i + 1  # Retorna o índice onde o pivô foi colocado.


nums = [2, 0, 5, 1, 4, 3]
quicksort(nums)
print(nums)