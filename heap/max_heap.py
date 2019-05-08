class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        last_element = len(self.storage) - 1
        # insert incoming value at end of array
        self.storage.append(value)
        self._bubble_up(last_element)

    def delete(self):
        last_element = len(self.storage) - 1
        # last element in array swaps with first element in array
        self.storage[0], self.storage[last_element] = self.storage[last_element], self.storage[0]
        # remove priority element (now last element)
        self.storage.pop(last_element)
        # now soft down new priority element
        self._sift_down(0)
        pass

    def get_max(self):
        return self.storage[0]

    def get_size(self):
        return len(self.storage)

    # index parameter is the index of the node whereever it is in the array
    def _bubble_up(self, index):
        # loop until the element reaches the top of the array
        # or we'll break the loop when we realize the element's priority is not larger than parent
        while index > 0:
            # the value at "index" fetches the index of its parent
            parent = (index - 1) // 2
            # check if the element at index has higher priority than the element at the parent index
            if self.storage[index] > self.storage[parent]:
                # swap elements
                self.storage[index], self.storage[parent] = self.storage[parent], self.storage[index]
                # we also need to update the index
                index = parent
            else:
                # otherwise, our element has reached a spot in the heap where its parent element has higher priority, stop climbing
                break

    def _sift_down(self, index):
        # left = 2 * index + 1
        # right = 2 * index + 2
        pass


'''
insert will stick the value at the end of the array
bubble up will be used by insert to move the element to it's proper spot

delete will delete the main root and moves a leaf to the main node
sift down will move the element down to it's proper spot
'''
