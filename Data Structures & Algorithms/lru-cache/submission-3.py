class Node:
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.next : Optional[Node] = None
        self.prev : Optional[Node] = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left
        self.size = 0

    def append(self, Node):
        self.right.prev.next = Node
        Node.prev = self.right.prev
        Node.next = self.right
        self.right.prev = Node
        self.size += 1

    def remove(self, Node):
        Node.prev.next = Node.next
        Node.next.prev = Node.prev
        self.size -= 1

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        self.remove(self.cache[key])
        self.append(self.cache[key])

        return self.cache[key].val
        

    def put(self, key: int, value: int) -> None:
        # Not adding a new node, just overwriting the value
        if key in self.cache:
            self.cache[key].val = value
            self.remove(self.cache[key])
            self.append(self.cache[key])
            return

        if self.size == self.capacity:
            first_node = self.left.next
            self.cache.pop(first_node.key)
            self.remove(first_node)
        new_node = Node(key, value)
        self.cache[key] = new_node
        self.append(new_node)
