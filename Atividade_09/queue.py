# Singly Linked List – Lista Simplesmente Encadeada para Fila (Queue)
# Apenas com as operações insert_at_end e delete_at_start

class Node:
    def __init__(self, data):
        self.data = data    # Valor do nó
        self.next = None    # Ponteiro para o próximo nó

class SinglyLinkedList:
    def __init__(self):
        self.head = None  # Início da fila (start)
        self.tail = None  # Final da fila (end)
        self.size = 0

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.tail is None:  # Fila vazia
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node # último nó atual aponta para o novo
            self.tail = new_node # tail aponta para o novo
        self.size += 1

    def delete_from_start(self):
        if self.head is None:
            raise IndexError("Fila vazia - não é possível remover")

        removed_data = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None  # Fila ficou vazia
        self.size -= 1
        return removed_data

    def peek_at_start(self):
        if self.head is None:
            raise IndexError("Fila vazia - não há elemento no início")
        return self.head.data

    def peek_at_end(self):
        if self.tail is None:
            raise IndexError("Fila vazia - não há elemento no final")
        return self.tail.data

    def is_empty(self):
        return self.size == 0


# Implementação da Fila usando a Lista Simplesmente Encadeada

class Queue:
    def __init__(self):
        self.linked_list = SinglyLinkedList()

    def enqueue(self, data):
        self.linked_list.insert_at_end(data)

    def dequeue(self):
        return self.linked_list.delete_from_start()

    def peek_start(self):
        valor = self.linked_list.peek_at_start()
        print(f"Início da fila: {valor}")
        return valor

    def peek_end(self):
        valor = self.linked_list.peek_at_end()
        print(f"Final da fila: {valor}")
        return valor

    def is_empty(self):
        return self.linked_list.is_empty()

    def size(self):
        print(f"Tamanho da fila: {self.linked_list.size}")
        return self.linked_list.size

    def __str__(self):
        if self.linked_list.is_empty():
            return "Fila vazia"

        atual = self.linked_list.head
        elementos = []
        while atual:
            elementos.append(str(atual.data))
            atual = atual.next

        elementos[0] += " (Início)"
        elementos[-1] += " (Fim)"
        return "\n↓\n".join(elementos)


# Testando a Fila
if __name__ == "__main__":
    fila = Queue()
    fila.enqueue("Cebola")
    fila.enqueue("Salada")
    fila.enqueue("Melancia")

    print(" ")
    print(fila)
    print(" ")

    fila.peek_start()
    fila.peek_end()

    print("\nRemovendo:")
    print(fila.dequeue())
    print(fila.dequeue())

    print("\nEstado atual da fila:")
    print(fila)

    fila.enqueue("Tomate")
    fila.enqueue("Cenoura")

    print("\nEstado atual da fila:")
    print(fila)
    print(" ")

    fila.size()
    print("A fila está vazia?", fila.is_empty())

    print("\nRemovendo todos:")
    print(fila.dequeue())
    print(fila.dequeue())
    print(fila.dequeue())

    print("\nA fila está vazia?", fila.is_empty())
    try:
        fila.peek_start()
    except IndexError as e:
        print(e)
