from stack import Stack

class QueueUsingStacks:
    """
    IMPLEMENTAR O COMPORTANMENTO DE FILAS USANDO APENAS OPERAÇÕES DE PILHAS.
    Fila (Queue) implementada usando pilha (Stack)
    para manter o comportamento FIFO (First In, First Out).
    Implementar apenas enqueue, dequeue e is_empty abaixo.
    """
    def __init__(self):
        self.pilha_principal = Stack()   # Pilha onde inserimos os elementos.
        self.pilha_aux = Stack()         # Pilha auxiliar que deve ser usada.

    def enqueue(self, data):
        while not self.pilha_aux.is_empty():
            self.pilha_principal.push(self.pilha_aux.pop())

        self.pilha_principal.push(data)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Fila vazia - Impossível remover elemento")

        while not self.pilha_principal.is_empty():
            self.pilha_aux.push(self.pilha_principal.pop())

        return self.pilha_aux.pop()


    def is_empty(self):
        return self.pilha_principal.is_empty() and self.pilha_aux.is_empty()

    def __str__(self):
        temp_principal = Stack()
        temp_aux = Stack()
        result = []

        while not self.pilha_aux.is_empty():
            val = self.pilha_aux.pop()
            result.append(val)
            temp_aux.push(val)

        while not self.pilha_principal.is_empty():
            val = self.pilha_principal.pop()
            temp_principal.push(val)

        while not temp_principal.is_empty():
            val = temp_principal.pop()
            result.append(val)
            self.pilha_principal.push(val)

        while not temp_aux.is_empty():
            self.pilha_aux.push(temp_aux.pop())

        if not result:
            return "Fila vazia"

        result[0] = f"{result[0]} (Início)"
        result[-1] = f"{result[-1]} (Fim)"
        return "\n↓\n".join(str(x) for x in result)


# Testando a fila
if __name__ == "__main__":
    fila = QueueUsingStacks()

    print("\nInserindo: 10, 20, 30")
    fila.enqueue(10)
    fila.enqueue(20)
    fila.enqueue(30)

    print(fila)

    print("\nRemovendo dois elementos:")
    print(fila.dequeue())
    print(fila.dequeue())
    fila.enqueue(40)

    print("\nEstado atual da fila:")
    print(fila)

    print("\nA fila está vazia?", fila.is_empty())

    print("\nRemovendo mais um elemento:")
    print(fila.dequeue())

    print("\nA fila está vazia?", fila.is_empty())

    print(" ")
    print(fila)