class Node:
    def __init__(self, data):
        self.data = data      # Valor do nó
        self.next = None      # Ponteiro para o próximo nó


class SingleLinkedList:
    def __init__(self):
        self.head = None      # Ponteiro para o início da lista
        self.tail = None      # Ponteiro para o final da lista (para facilitar append)
        self.size = 0         # Tamanho da lista

    def append(self, data):
        """
        Adiciona um novo nó (Node) ao final da lista encadeada.

        Objetivo:
            - Criar um novo nó contendo o valor fornecido.
            - Inserir esse nó após o último elemento (tail).
            - Atualizar os ponteiros `head`, `tail` e o contador `size`.
            - Não esquecer de verificar se a lista está vazia e tratar de acordo.
            - Utilizar as estruturas já criadas acima de NODE e SingleLinkedList, 
                self.data, self.next, self.head, self.tail, self.size


        Observações:
            - Esse método deve ser O(1), pois usamos o ponteiro tail 
              para evitar percorrer a lista inteira.
            - É importante atualizar a tail corretamente, senão a lista
              "perde" o final.

        Exemplo esperado:
            lista = SingleLinkedList()
            lista.append(10)   # head=10, tail=10
            lista.append(20)   # head=10, tail=20
            lista.append(30)   # head=10, tail=30
            print(lista)       # "10 -> 20 -> 30"
        """
        novo_no = Node(data)

        if self.head is None:
            self.head = self.tail = novo_no
        else:
            self.tail.next = novo_no
            self.tail = novo_no

        self.size += 1

    def insert(self, index, data):
        """
        Insere um novo nó na posição desejada (base 0) da lista.

        Objetivo:
            - Criar um novo nó contendo o valor fornecido.
            - Inserir esse nó na posição indicada pelo índice.
            - Atualizar os ponteiros necessários e o contador `size`.
            - A teoria e explicação foi dada na aula passada.
            - Não esquecer de verificar se a lista está vazia e tratar de acordo.

        Exemplo esperado:
            lista = SingleLinkedList()
            lista.append(5)
            lista.append(23)
            lista.append(7)
            lista.insert(1, 11)   # Insere o 11 na posição 1
            print(lista)          # "5 -> 11 -> 23 -> 7"
        """
        novo_no = Node(data)

        if self.head is None:
            self.head = self.tail = novo_no

        elif index == 0:
            novo_no.next = self.head
            self.head = novo_no
            
        else:
            ponteiro = self.head
            for i in range(index - 1):
                ponteiro = ponteiro.next

            novo_no.next = ponteiro.next
            ponteiro.next = novo_no

            if novo_no.next is None:
                self.tail = novo_no
        self.size += 1

    def __str__(self):
        """
        Retorna uma representação string da lista (ex: 5 -> 23 -> 7 -> 13).
        """
        elements = []
        trav = self.head  
        while trav:
            elements.append(str(trav.data))
            trav = trav.next
        return " -> ".join(elements)


# Criando a lista inicial: 5 -> 23 -> 7 -> 13
linked_list = SingleLinkedList()
linked_list.append(5)
linked_list.append(23)
linked_list.append(7)
linked_list.append(13)

print("Lista original:")
print(linked_list)

# Inserindo 11 na terceira posição (índice 2, entre 23 e 7)
linked_list.insert(2, 11)

print("\nLista após inserir 11 na terceira posição:")
print(linked_list)