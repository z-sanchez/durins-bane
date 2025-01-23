BUCKET_SIZE = 7

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash(self,value):
        return value % self.size
    
    def addItem(self, value):
        index = self.hash(value)
        self.table[index].append(value)

    def deleteItem(self, value):
        index = self.hash(value)
        self.table[index].remove(value)

    def printTable(self):
        for x in range(self.size):
            print(self.table[x])
        



if __name__ == "__main__":
    print("What's up")
    items = [5, 12 ,9 ,8 ,33]
    hashTable = HashTable(BUCKET_SIZE)

    for x in items:
        hashTable.addItem(x)


    hashTable.addItem(55)
    hashTable.deleteItem(12)
    hashTable.printTable()

    