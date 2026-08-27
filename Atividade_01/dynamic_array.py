class DynamicIntArray:
    def __init__(self, capacity=2):
        if capacity <= 0:
            raise ValueError("Capacidade inicial deve ser maior que 0.")
        self.capacity = capacity        # Tamanho real do array interno
        self.size = 0                   # Quantos elementos o usuário colocou
        self.data = [0] * self.capacity # Cria Array estático interno (só de inteiros)

    def is_empty(self):
        return self.size == 0

    def get(self, index):
        if index < 0 or index >= self.size:
            raise IndexError('Indice fora dos limites')
        return self.data[index]

    def set(self, index, value):
       if index < 0 or index >= self.size:
           raise IndexError('Valor inválido')
       else:
           self.data[index] = value
       
    def append(self, value):
        if self.size == self.capacity:
            self._resize(new_capacity=self.capacity * 2)

        self.data[self.size] = value
        self.size += 1
        print(f"data interno: {self.data}")

    def _resize(self, new_capacity):
        if new_capacity > self.capacity:
            print(f"⏫ Redimensionando de {self.capacity} para {new_capacity}")
        else:
            print(f"⏬ Redimensionando de {self.capacity} para {new_capacity}")
        new_data = [0] * new_capacity
        for i in range(self.size):
            new_data[i] = self.data[i]
        self.data = new_data
        self.capacity = new_capacity

    def __str__(self):
        return str(self.data[:self.size])

    def remove_at(self, index):
        """
        Remove e retorna o elemento no índice informado, deslocando os seguintes à esquerda.

        Parâmetros:
            index (int): Índice do elemento a remover (0 <= index < size).

        Retorno:
            int: Valor removido. (Retornar o Valor Removido)

        Exceções:
            IndexError: se index estiver fora dos limites.

        Detalhes:
            - Após remover, se size <= 1/4 capacity (mínimo 2) chama _resize.
        """
        if index < 0 or index >= self.size:
            raise IndexError("Indice Fora dos Limites.")

        valor_removido = self.data[index]
        for i in range(index, self.size - 1):
            self.data[i] = self.data[i + 1]

        self.size -=1

        if self.size <= self.capacity // 4 and self.capacity > 2:
            nova_capacidade = max(2, self.capacity // 2)
            self._resize(nova_capacidade)
        return valor_removido


lista = DynamicIntArray()


#============ SAIDAS DE TESTE ============

if lista.is_empty():
    print("Lista vazia!")
else:
    print("Lista tem elementos.")

print("Adicionando o 10;")
lista.append(10)
print("Lista: ", lista) 

print("Adicionando o 20;")
lista.append(20)
print("Lista: ", lista)

print("Adicionando o 30;")
lista.append(30)
print("Lista: ", lista)
print("Tamanho da Lista para o usuário: ", lista.size)
print("Tamanho real (capacidade) da Lista internamente: ", lista.capacity)

print("Adicionando o 40;")
lista.append(40)
print("Lista: ", lista)

print("Adicionando o 50;")
lista.append(50)
print("Lista: ", lista)        

print("Elemento na posição 2: ", lista.get(2))    

print("Trocando elemento no índice 2 para 99.")   
lista.set(2, 99)
print("Lista: ", lista)       


print("Removendo elemento no indice 1 se existir.") 
lista.remove_at(1) 
print("Lista: ", lista)

print("Removendo mais um elementos no indice 2.") 
lista.remove_at(2)
print("Lista: ", lista)

print("Removendo mais um elementos no indice 0.") 
lista.remove_at(0)
print("Lista: ", lista)