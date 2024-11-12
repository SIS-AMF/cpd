class Produto:
    def __init__(self, id, nome, descricao, preco):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.preco = preco
        self.left = None
        self.right = None

class ABB:
    def __init__(self):
        self.root = None

    # Inserir um novo produto na BST
    def inserir(self, id, nome, descricao, preco):
        novo_produto = Produto(id, nome, descricao, preco)
        if not self.root:
            self.root = novo_produto
        else:
            self._inserir_recursivo(self.root, novo_produto)

    def _inserir_recursivo(self, node, novo_produto):
        if novo_produto.id < node.id:
            if node.left:
                self._inserir_recursivo(node.left, novo_produto)
            else:
                node.left = novo_produto
        else:
            if node.right:
                self._inserir_recursivo(node.right, novo_produto)
            else:
                node.right = novo_produto

    # Buscar um produto pelo ID
    def buscar(self, id):
        return self._buscar_recursivo(self.root, id)

    def _buscar_recursivo(self, node, id):
        if not node or node.id == id:
            return node
        if id < node.id:
            return self._buscar_recursivo(node.left, id)
        return self._buscar_recursivo(node.right, id)

    # Remover um produto pelo ID
    def remover(self, id):
        self.root = self._remover_recursivo(self.root, id)

    def _remover_recursivo(self, node, id):
        if not node:
            return node
        if id < node.id:
            node.left = self._remover_recursivo(node.left, id)
        elif id > node.id:
            node.right = self._remover_recursivo(node.right, id)
        else:
            # Caso 1: Nó sem filhos
            if not node.left and not node.right:
                return None
            # Caso 2: Nó com um filho
            elif not node.left:
                return node.right
            elif not node.right:
                return node.left
            # Caso 3: Nó com dois filhos
            min_maior = self._minimo(node.right)
            node.id, node.nome, node.descricao, node.preco = min_maior.id, min_maior.nome, min_maior.descricao, min_maior.preco
            node.right = self._remover_recursivo(node.right, min_maior.id)
        return node

    def _minimo(self, node):
        while node.left:
            node = node.left
        return node

    # Listar os produtos em ordem crescente de ID
    def listar_em_ordem(self):
        produtos = []
        self._in_order_recursivo(self.root, produtos)
        for produto in produtos:
            print(f"ID: {produto.id}, Nome: {produto.nome}, Preço: {produto.preco}")

    def _in_order_recursivo(self, node, produtos):
        if node:
            self._in_order_recursivo(node.left, produtos)
            produtos.append(node)
            self._in_order_recursivo(node.right, produtos)


arvore = ABB()
arvore.inserir(30, "Produto 1", "Descrição do produto 1", 100.0)
arvore.inserir(20, "Produto 2", "Descrição do produto 2", 200.0)
arvore.inserir(40, "Produto 3", "Descrição do produto 3", 150.0)


produto = arvore.buscar(20)
if produto:
    print(f"Produto encontrado: {produto.nome}, Preço: {produto.preco}")
else:
    print("Produto não encontrado")


print("\nProdutos em ordem crescente de ID:")
arvore.listar_em_ordem()


arvore.remover(30)
print("\nProdutos após remoção do ID 30:")
arvore.listar_em_ordem()
