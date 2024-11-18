class Hash:
    def __init__(self):
        self.table = {}

    def _hash(self, key):
        return int(key) % 10

    def insert(self, key, value):
        index = self._hash(key)
        print(index)
        if self.table.get(index) is None:
            self.table[index] = [(key, value)]
            return
        self.table[index].append((key, value))

    def search(self, key):
        index = self._hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None

db = Hash()
db.insert("20", "Lucas")
db.insert("42", "Sonia")
db.insert("19", "Vitoria")
db.insert("14", "Erike")
db.insert("0", "Jose")


print(db.table)
print(db.search("0"))
