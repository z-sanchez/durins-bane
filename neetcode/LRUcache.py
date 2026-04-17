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

        # left is the least recently used node, won't hold any actual data
        self.left = Node(0, 0)
        # right is the most recently used node, won't hold any actual data
        self.right = Node(0, 0)

        # connect nodes left to right
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        prev = node.prev
        next = node.next

        # remove node by skipping over it (prev -> next)
        prev.next = next
        next.prev = prev

    def insert(self, node):
        # insert node before the right (most recently used)
        prev = self.right.prev
        next = self.right

        # node goes between prev and next
        prev.next = node
        next.prev = node
        node.next = next
        node.prev = prev

    def get(self, key: int) -> int:
        if key in self.cache:
            # remove node from its current position
            self.remove(self.cache[key])

            # insert node at the right (most recently used)
            self.insert(self.cache[key])

            return self.cache[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        # if key already exists, remove it
        if key in self.cache:
            self.remove(self.cache[key])

        # set new node in cache and insert it at the right (most recently used)
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        # if cache exceeds capacity, remove least recently used node (left.next)
        if len(self.cache) > self.size:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
