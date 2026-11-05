    # Percurso em PÓS ORDEM ("left, right, root")
    def postorder_traversal(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            self.postorder_traversal(node.left)
        if node.right:
            self.postorder_traversal(node.right)
        print(node)

    # Percurso em PRÉ-ORDEM ("root, left, right")
    def preorder_traversal(self, node=None):
        if node is None:
            node = self.root
        print(node)
        if node.left:
            self.preorder_traversal(node.left)
        if node.right:
            self.preorder_traversal(node.right)

    # Percurso em nível (Level-order/Breadth-first)
    def levelorder_traversal(self, node=None):
        if node is None:
            node = self.root

        q = Queue()
        q.enqueue(node)

        while not q.is_empty():
            atual = q.dequeue()      # tira o da frente da fila
            print(atual)             # "visita" o nó
            if atual.left:
                q.enqueue(atual.left)
            if atual.right:
                q.enqueue(atual.right)