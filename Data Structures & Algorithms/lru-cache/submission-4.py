class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next : Node = None
        self.prev : Node = None

class LRUCache:
    def __init__(self, capacity: int):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.size = 0
        self.map = {}

    def remove(self, node: Node) -> Node:
        node.next.prev = node.prev
        node.prev.next = node.next
        node.next = None
        node.prev = None
        self.size -= 1
        return node

    def append(self, node: Node):
        self.tail.prev.next = node       
        node.prev = self.tail.prev
        self.tail.prev = node
        node.next = self.tail
        self.size += 1

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        node = self.remove(self.map[key])
        self.append(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        node : Node = None
        if key in self.map:
            node = self.remove(self.map[key])
            node.val = value
        else:
            node = Node(key, value)
            self.map[key] = node
            if self.size == self.capacity:
                removed_node = self.remove(self.head.next)
                self.map.pop(removed_node.key)
        self.append(node)