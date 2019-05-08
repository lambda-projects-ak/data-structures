class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        pass

    def delete(self):
        # remove priority element
        # last element in array swaps with new open space
        # now soft down new priority element
        pass

    def get_max(self):
        # get priority element and return it O(1)
        pass

    def get_size(self):
        # len(arr)?
        pass

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
