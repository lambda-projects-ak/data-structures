
# each node is it's own BST instance, it only knows about it's children nodes


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # assess left tree
        if value < self.value:
            if not self.left:
                self.left = BinarySearchTree(value)
            # run insert on left node if available
            else:
                self.left.insert(value)

        # assess right tree
        elif value > self.value:
            if not self.right:
                self.right = BinarySearchTree(value)
            # run insert on right node if available
            else:
                self.right.insert(value)

    def contains(self, target):
        if target == self.value:
            return True
        # check left node
        elif target < self.value and self.left:
            return self.left.contains(target)
        # check right node
        elif target > self.value and self.right:
            return self.right.contains(target)
        # no match
        else:
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
        cb(self.value)

        if self.left and self.right:
            self.left.for_each(cb)
            self.right.for_each(cb)

        if self.left:
            self.left.for_each(cb)

        if self.right:
            self.right.for_each(cb)
