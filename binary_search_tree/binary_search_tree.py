
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
        if target == self.value:
            return True
        elif target < self.value and self.left:
            return self.left.contains(target)
        elif target > self.value and self.right:
            return self.right.contains(target)
        elif target != self.value:
            return False

    def get_max(self):
        # current_node = self
        # max_value = 0

        # while max_value < current_node.value:
        #     current_node = current_node.right
        #     if max_value < current_node.value:
        #         max_value = current_node.value

        # return max_value
        pass

    def for_each(self, cb):
        pass
