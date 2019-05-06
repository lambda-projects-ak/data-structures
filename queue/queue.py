
class Queue:
    def __init__(self):
        self.size = 0
        # what data structure should we
        # use to store queue elements?
        self.storage = []

    def enqueue(self, item):
        self.size += 1
        return self.storage.insert(0, item)

    def dequeue(self):
        if self.size > 0:
            self.size -= 1
            return self.storage.pop(len(self.storage) - 1)

    def len(self):
        if self.size > 0:
            return len(self.storage)
        else:
            return 0

# To optimize for inserting and deleting, a linked list could be used


test = Queue()
print(test.storage)

test.enqueue(1)

print(test.storage)

# test.dequeue()

# print(test.storage)


print(test.len())


class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

# Queue would be a linked list
# Back of line (head)
# Front of line (tail)


class QueueLL:
    def __init__(self):
        self.size = 0
        # what data structure should we
        # use to store queue elements?
        self.storage = []
        self.head = None
        self.tail = None

    def enqueue(self, item):
        # what if the queue is empty?
        if not self.head and not self.tail:
            # set incoming node to head and tail
            self.head = Node(item)
            self.tail = Node(item)
        # what if the queue has one item?
            # update head to point to new node
            # point new node to tail
        # what if the queue has multiple
            # create a node, point it to old head
        pass

    def dequeue(self):
        # what if queue is empty?
            # return None
        # what if queue has one item?
            # remove reference from queue, head = None, tail = None
        # what if queue has multiple items?
            # iterate through items until you reach the end, remove the reference from the second to last node
            # update tail to second to last node
        pass

    def len(self):
        # use size variable
        # while node reference is not None
            # increment size by 1
        pass
