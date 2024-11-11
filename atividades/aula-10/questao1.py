class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class ABB:
    def __init__(self):
        self.root = None

    # Função de inserção
    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left:
                self._insert_recursive(node.left, value)
            else:
                node.left = Node(value)
        else:
            if node.right:
                self._insert_recursive(node.right, value)
            else:
                node.right = Node(value)

    # Função de busca
    def search(self, value):
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        if not node or node.value == value:
            return node
        if value < node.value:
            return self._search_recursive(node.left, value)
        return self._search_recursive(node.right, value)

    # Função de deleção
    def delete(self, value):
        self.root = self._delete_recursive(self.root, value)

    def _delete_recursive(self, node, value):
        if not node:
            return node
        if value < node.value:
            node.left = self._delete_recursive(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursive(node.right, value)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            min_larger_node = self._get_min(node.right)
            node.value = min_larger_node.value
            node.right = self._delete_recursive(
                node.right, min_larger_node.value)
        return node

    def _get_min(self, node):
        while node.left:
            node = node.left
        return node

    # Funções de impressão
    def print_pre_order(self):
        print(self._pre_order_recursive(self.root))

    def _pre_order_recursive(self, node):
        if node is None:
            return []
        else:
            return [node.value] + self._pre_order_recursive(node.left) + self._pre_order_recursive(node.right)

    def print_in_order(self):
        print(self._in_order_recursive(self.root))

    def _in_order_recursive(self, node):
        if node is None:
            return []
        else:
            return self._in_order_recursive(node.left) + [node.value] + self._in_order_recursive(node.right)

    def print_post_order(self):
        print(self._post_order_recursive(self.root))

    def _post_order_recursive(self, node):
        if node is None:
            return []
        else:
            return self._post_order_recursive(node.left) + self._post_order_recursive(node.right) + [node.value]


# Exemplo de uso
tree = ABB()
tree.insert(10)
tree.insert(9)
tree.insert(8)
tree.insert(7)
tree.insert(6)
tree.insert(5)
tree.insert(4)

print("Pré-ordem:")
tree.print_pre_order()

print("Em-ordem:")
tree.print_in_order()

print("Pós-ordem:")
tree.print_post_order()

# Buscar um elemento
print("Busca pelo valor 7:", tree.search(7))

# Deletar um elemento
tree.delete(7)
print("Árvore após deletar o valor 7 (ordem simétrica):")
tree.print_in_order()
