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
        print(capacity)
        self.cache = {}
        self.capacity = capacity

        left = Node(0, 0)
        right = Node(0, 0)

        left.next = right
        right.prev = left

    def remove(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def insert(self, node):
        prev = self.right.prev
        next = self.right

        node.prev = prev
        node.next = next

        prev.next = node
        next.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
