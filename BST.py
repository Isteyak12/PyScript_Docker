class Node:
    def __init__(self, data, rate):
        self.data = data
        self.rate = rate
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None
        self.size = 0

    def insert1(self, current, data, rate):
        self.size += 1
        new_node = Node(data, rate)
        if current is None:
            return new_node
        if current.data > new_node.data:
            current.left = self.insert1(current.left, data, rate)
        else:
            current.right = self.insert1(current.right, data, rate)
        return current

    def insert(self, data, rate):
        self.root = self.insert1(self.root, data, rate)

    def print_tree(self, current):
        if current:
            self.print_tree(current.left)
            print(f"Data: {current.data}, Rate: {current.rate}")
            self.print_tree(current.right)


# Test your code in the main section
b1 = BST()
b1.insert(0, "kart")
b1.insert(1, "bull")
b1.print_tree(b1.root)
