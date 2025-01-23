BUCKET_SIZE = 5

class Hash:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hashFunction(self, value): #division hash
        # remainder will always be less than table size
        return value % self.size
    
    def insertItem(self, value):
        index = self.hashFunction(value)

        # insert will regrow the list causing issues with our class size
        # self.table.insert(index,value)

        self.table[index].append(value)

    def deleteItem(self, value):
        index = self.hashFunction(value)
        self.table[index].remove(value)
       

    def displayHash(self):
        for x in self.table:
            print(x)


# Drive Program
if __name__ == "__main__":
    # array that contains keys to be mapped
    a = [15, 11, 27, 8, 12, 25]

    # Create a empty has of BUCKET_SIZE
    h = Hash(BUCKET_SIZE)

    # insert the keys into the hash table
    for x in a:
        h.insertItem(x)

    h.deleteItem(8)

    # Display the hash table
    h.displayHash()