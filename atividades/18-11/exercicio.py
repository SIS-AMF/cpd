class File:
    def __init__(self, name, path, size):
        self.name = name
        self.path = path
        self.size = size

    def __repr__(self):
        return f"File(name='{self.name}', path='{self.path}', size={self.size} KB)"


class Hash:
    def __init__(self, size=10):
        self.size = size
        self.table = {i: [] for i in range(size)}

    def _hash(self, key):
        return sum(ord(char) for char in key) % self.size

    def add(self, file):
        """Adiciona um arquivo à tabela hash."""
        index = self._hash(file.name)
        for f in self.table[index]:
            if f.name == file.name:
                f.path = file.path
                f.size = file.size
                return
        self.table[index].append(file)

    def search(self, name):
        """Busca um arquivo pelo nome."""
        index = self._hash(name)
        for file in self.table[index]:
            if file.name == name:
                return file
        return None

    def remove(self, name):
        """Remove um arquivo pelo nome."""
        index = self._hash(name)
        self.table[index] = [file for file in self.table[index] if file.name != name]

    def list_files(self):
        """Lista todos os arquivos na tabela hash."""
        files = []
        for bucket in self.table.values():
            files.extend(bucket)
        return files


if __name__ == "__main__":
    ht = Hash(size=10)

    file1 = File("relatorio.pdf", "/documentos/relatorio.pdf", 1024)
    file2 = File("foto.jpg", "/imagens/foto.jpg", 2048)
    file3 = File("dados.csv", "/planilhas/dados.csv", 512)
    file4 = File("backup.zip", "/backup/backup.zip", 4096)

    ht.add(file1)
    ht.add(file2)
    ht.add(file3)
    ht.add(file4)

    print("Buscar 'dados.csv':", ht.search("dados.csv"))

    ht.remove("foto.jpg")
    print("\nArquivo 'foto.jpg' removido.")

    print("\nArquivos restantes:")
    for file in ht.list_files():
        print(file)
