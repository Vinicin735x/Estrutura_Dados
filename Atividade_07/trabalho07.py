def h_index_linear_decrescente(citacoes):
    h = 0
    for i in range(len(citacoes)):
        if citacoes[i] >= i + 1:
            h = i + 1
        else:
            break  # lista decrescente: os próximos também vão falhar
    return h


def h_index_binaria_decrescente(citacoes):
    inicio = 0
    fim = len(citacoes) - 1
    h = 0

    while inicio <= fim:
        meio = (inicio + fim) // 2
        if citacoes[meio] >= meio + 1:
            h = meio + 1        # essa posição serve, guarda como candidato
            inicio = meio + 1   # tenta achar um h maior à direita
        else:
            fim = meio - 1      # não serve, a fronteira está à esquerda
    return h

citacoesExemplo = [1, 1]

citacoesLazaro = [43, 24, 6, 3, 3, 2, 1, 1]
citacoesFelizardo = [30, 16, 14, 9, 6, 6, 5, 4, 2, 2, 2]
citacoesEduardo = [39, 24, 20, 13, 12, 9, 7, 6, 6, 5, 2, 2, 2, 0, 0, 0, 0, 0, 0]

print("Busca Linear (h-index) Exemplo:", h_index_linear_decrescente(citacoesExemplo))
print("Busca Binária (h-index) Exemplo:", h_index_binaria_decrescente(citacoesExemplo))
print()
print("Busca Linear (h-index) Felizardo:", h_index_linear_decrescente(citacoesFelizardo))
print("Busca Binária (h-index) Felizardo:", h_index_binaria_decrescente(citacoesFelizardo))
print()
print("Busca Linear (h-index) Lazaro:", h_index_linear_decrescente(citacoesLazaro))
print("Busca Binária (h-index) Lazaro:", h_index_binaria_decrescente(citacoesLazaro))
print()
print("Busca Linear (h-index) Eduardo:", h_index_linear_decrescente(citacoesEduardo))
print("Busca Binária (h-index) Eduardo:", h_index_binaria_decrescente(citacoesEduardo))
