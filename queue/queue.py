
# class Queue:
#     def __init__(self):
#         self.size = 0
#         # what data structure should we
#         # use to store queue elements?
#         self.storage = []

#     def enqueue(self, item):
#         self.size += 1
#         return self.storage.insert(0, item)

#     def dequeue(self):
#         if self.size > 0:
#             self.size -= 1
#             return self.storage.pop(len(self.storage) - 1)

#     def len(self):
#         if self.size > 0:
#             return len(self.storage)
#         else:
#             return 0

# # To optimize for inserting and deleting, a linked list could be used


class Node:
    def __init__(self, name, next_node=None):
        self.name = name
        self.next_node = next_node

    def get_name(self):
        return self.name

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

# Queue would be a linked list


class Queue:
    def __init__(self):
        self.size = 0
        # what data structure should we
        # use to store queue elements?
        self.storage = []
        self.head = None
        self.tail = None

    def enqueue(self, node):
        new_node = Node(node)
        # what if the queue is empty?
        if not self.head and not self.tail:
            # set incoming node to head and tail
            self.head = new_node
            self.tail = new_node
        # what if the queue has nodes?
        else:
            # set current tail next to new node
            self.tail.set_next(new_node)
            # update tail with new node
            self.tail = new_node

    def dequeue(self):
        dequeue_node = self.head
        # what if queue is empty?
        if not self.head and not self.tail:
            return None
        # what if queue has one node?
        if self.head == self.tail:
            # remove reference from queue, head = None, tail = None
            self.head = None
            self.tail = None
        # what if queue has multiple nodes?
        else:
            self.head = self.head.get_next()

        return dequeue_node.get_name()

    def len(self):
        count = 0
        current_node = self.head
        while current_node != None:
            count += 1
            current_node = current_node.get_next()
        return count
