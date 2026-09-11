class Node:
    def __init__(self, value = None):
        self.val = value
        self.children = []


class PrefixTree:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        cur_node = self.root
        for char in word:
            found_node = False
            for node in cur_node.children:
                if node.val == char:
                    cur_node = node
                    found_node = True
                    break
            if found_node:
                continue
            
            new_node = Node(char)
            cur_node.children.append(new_node)
            cur_node = new_node

        cur_node.children.append(Node('0'))

    def search(self, word: str) -> bool:
        cur_node = self.root
        word += '0'
        for char in word:
            for node in cur_node.children:
                if node.val == char:
                    cur_node = node
                    break
            else:
                return False
        return True

    def startsWith(self, prefix: str) -> bool:
        cur_node = self.root
        for char in prefix:
            for node in cur_node.children:
                if node.val == char:
                    cur_node = node
                    break
            else:
                return False
        return True

        
        