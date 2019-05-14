"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is point to."""

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def add_to_head(self, value):
        new_node = ListNode(value)

        # ll is empty - assign new node to both head and tail
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
            self.length += 1

        # ll has more than one node
        else:
            self.head.insert_before(value)
            self.head = self.head.prev
            self.length += 1

    def remove_from_head(self):
        # ll has no nodes
        if not self.head and not self.tail:
            return None

        # ll has one node
        elif self.head == self.tail:
            removed = self.head.value
            self.head = None
            self.tail = None
            self.length -= 1
            return removed

        # ll has head, update head to none, update new head prev to none
        else:
            removed = self.head.value
            self.head = self.head.next
            self.head.prev = None
            self.length -= 1
            return removed

    def add_to_tail(self, value):
        new_node = ListNode(value)

        # ll is empty - assign new node to both head and tail
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
            self.length += 1

        # ll has more than one node
        else:
            self.tail.insert_after(value)
            self.tail = self.tail.next
            self.length += 1

    def remove_from_tail(self):
        # ll has no nodes
        if not self.head and not self.tail:
            return None
        # ll has one node
        elif self.head == self.tail:
            removed = self.tail.value
            self.head = None
            self.tail = None
            self.length -= 1
            return removed
        else:
            removed = self.tail.value
            self.tail = self.tail.prev
            self.tail.next = None
            self.length -= 1
            return removed

    def move_to_front(self, node):
        # insert current node before head
        self.add_to_head(node.value)
        # delete incoming node from list
        self.delete(node)

    def move_to_end(self, node):
        # insert current node after tail
        self.add_to_tail(node.value)
        # delete incoming node from list
        self.delete(node)

    def delete(self, node):
        # ll has one node
        if self.head == self.tail:
            self.remove_from_head()

        elif self.head == node:
            self.remove_from_head()

        elif self.tail == node:
            self.remove_from_tail()
        # if ll has more than one node
        else:
            node.delete()
            self.length -= 1

    def get_max(self):
        max_value = self.head.value
        current = self.head
        while current.next != None:
            current = current.next
            if current.value > max_value:
                max_value = current.value
        return max_value


ll = DoublyLinkedList()

another_node = ListNode(4)  # None, 4, None
# print(new_node.prev)

ll.add_to_head(4)
