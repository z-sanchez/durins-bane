# Time Complexity: O(1) for get and put operations
# Space Complexity: O(n), where n is the capacity of the cache


class Node:
    def __init__(self, key, val):
        self.key = key  # key is the key to the node in the cache
        self.value = val  # value is our actual value
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.cache = {}

        self.left = Node(0, 0)
        self.right = Node(0, 0)

        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        next = node.next
        prev = node.prev

        prev.next = next
        next.prev = prev

    def insert(self, node):
        prev = self.right.prev
        next = self.right

        prev.next = node
        next.prev = node

        node.next = next
        node.prev = prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        newNode = Node(key, value)
        self.cache[key] = newNode
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
