
class LowLevelHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None for _ in range(size)]

    def hash(self, value):
        return value % self.size
    
    def insert(self,value):
        index = self.hash(value)
        self.table[index] = value

    def has(self, value):
        index = self.hash(value)

        if self.table[index] == value:
            return True
        else:
            return False



def checkDuplicatesLowLevel():
    nums = [1,2,3,3]
    hashTable = LowLevelHashTable(len(nums))

    for x in nums:
        if (hashTable.has(nums[x])):
            return True
        else:
            hashTable.insert(nums[x])
        
    return False


def checkDuplicatesHighLevel():
    nums = [1,2,3,3]
    seen = set()

    # add and in for set are O(n)

    for x in nums:
        if x in seen:
            return True
        seen.add(x)

    return False

lowLevelResult = checkDuplicatesLowLevel()    
print("Has Duplicates (low level):",lowLevelResult)
highLevelResult = checkDuplicatesHighLevel()    
print("Has Duplicates (high level):",highLevelResult)


