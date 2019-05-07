
# each node is it's own BST instance, it only knows about it's children nodes


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # create new node if conditions are met
        if value <= self.value and not self.left:
            self.left = BinarySearchTree(value)
        elif value >= self.value and not self.right:
            self.right = BinarySearchTree(value)

        # recursive logic
        elif value <= self.value:
            self.left.insert(value)
        elif value >= self.value:
            self.right.insert(value)

    def contains(self, target):
        pass

    def get_max(self):
        pass

    def for_each(self, cb):
        pass
