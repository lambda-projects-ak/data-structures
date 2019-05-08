
# each node is it's own BST instance, it only knows about it's children nodes


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if not self.left:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)

        elif value > self.value:
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    def contains(self, target):
        if target == self.value:
            return True
        elif target < self.value and self.left:
            return self.left.contains(target)
        elif target > self.value and self.right:
            return self.right.contains(target)
        elif target != self.value:
            return False

    def get_max(self):
        # if the current node has no right child, return the value
        if not self.right:
            return self.value
        # if there is a right node, it will be greater than current node
        # call get max again to set next node as current max
        else:
            return self.right.get_max()

    def for_each(self, cb):
        pass
