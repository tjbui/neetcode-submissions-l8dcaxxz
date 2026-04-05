class Node:
    def __init__(self, key, value):
        self.key, self.value = key, value
        self.next , self.prev = None, None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity, self.size = capacity, 0
        self.head, self.tail = Node(-1, -1), Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.d = {}

    def insert_end(self, node):
        self.tail.prev.next = node
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev = node

    def remove(self, node):
        prev, next = node.prev, node.next
        next.prev, prev.next = prev, next

    def get(self, key: int) -> int:
        if key not in self.d:
            return -1
        
        if self.d[key] == self.tail.prev:
            return self.d[key].value
        
        node = self.d[key]
        self.remove(node)
        self.insert_end(node)
        return self.d[key].value

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            self.d[key].value = value
            self.remove(self.d[key])
            self.insert_end(self.d[key])
            return
            
        if self.size == self.capacity:
            lru = self.head.next
            self.remove(lru)
            del self.d[lru.key]
            self.size -= 1

        node = Node(key, value)
        self.d[key] = node
        self.insert_end(node)
        self.size += 1

        
