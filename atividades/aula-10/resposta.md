### 2. Descrição de outros tipos de árvores

#### 2.1 Red–Black Tree (Árvore rubro-negra)
- **O que é?**: Uma Red-Black Tree é uma árvore binária de busca, onde cada nó tem uma cor: vermelho ou preto.
- **Para que serve?**: Ela é usada para manter as operações de inserção e remoção rápidas, garantindo que a árvore permaneça balanceada.
- **Como funciona?**: A árvore segue regras de cor que ajudam a manter o balanceamento:
  - A raiz e as folhas (nós nulos) são pretos.
  - Nós vermelhos não podem ter filhos vermelhos, evitando uma sequência de nós vermelhos.
  - Todos os caminhos da raiz até uma folha têm o mesmo número de nós pretos.
  
  Essas regras fazem com que a árvore não cresça demais de um lado só, o que mantém as operações rápidas.

#### 2.2 B-Tree
- **O que é?**: A B-Tree é uma árvore de busca balanceada, onde cada nó pode ter vários filhos, não só dois como em uma árvore binária.
- **Para que serve?**: É usada em bancos de dados e sistemas de arquivos para organizar grandes quantidades de dados de forma eficiente.
- **Como funciona?**: Cada nó contém várias chaves e pode ter múltiplos filhos. Quando um nó tem mais chaves do que o permitido, ele se divide em dois, mantendo a árvore equilibrada e com altura baixa. Isso permite que as buscas e inserções permaneçam rápidas mesmo com muitos dados.

#### 2.3 B+ Tree
- **O que é?**: A B+ Tree é uma variação da B-Tree, onde todos os valores ficam nas folhas e os nós internos guardam apenas chaves para guiar a busca.
- **Para que serve?**: Muito usada em sistemas de bancos de dados, ela é ideal para consultas de intervalos, onde precisamos acessar uma sequência de valores.
- **Como funciona?**: Na B+ Tree, todas as chaves e valores estão nas folhas, e as folhas são encadeadas em uma sequência. Isso facilita a navegação entre os dados de forma sequencial, além de manter o balanceamento, garantindo buscas rápidas.
