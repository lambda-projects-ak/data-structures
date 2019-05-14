Answer the following questions for each of the data structures you implemented as part of this project.

## Queue

1.  What is the runtime complexity of `enqueue`?
    appending to the end of the linked list, reassigning the tail
    runtime of O(1)

2.  What is the runtime complexity of `dequeue`?
    removing head node and reassigning head to the next node
    runtime of O(1)

3.  What is the runtime complexity of `len`?
    iterate over entire linked list
    runtime of O(n)

## Binary Search Tree

1. What is the runtime complexity of `insert`?
   insert checks one node per level all the way down the tree
   runtime of O(log(n))

2. What is the runtime complexity of `contains`?
   contains checks one node per level all the way down tree
   runtime of O(log(n))

3. What is the runtime complexity of `get_max`?
   get_get checks one node per level until it reaches the end of the right tree
   runtime of O(log(n))

## Heap

1. What is the runtime complexity of `_bubble_up`?
   single loop, comparing index with parent, checking one node per level, swapping
   runtime of O(log(n))

2. What is the runtime complexity of `_sift_down`?
   recursive with comparisons, only checking one node per level, performing swap
   runtime of O(log(n))

3. What is the runtime complexity of `insert`?
   inserting at end of a list
   runtime of O(1), not including the bubble method call
   worst case runtime would be O(n) if you run out space and need to move the entire array
   runtime of O(log(n)), including the bubble method call

4. What is the runtime complexity of `delete`?
   delete last item in array
   runtime of O(1), not including sift down
   runtime of O(log(n)), including sift down method call

5. What is the runtime complexity of `get_max`?
   getting first element on array
   runtime of O(1)

## Doubly Linked List

1. What is the runtime complexity of `ListNode.insert_after`?
   insertion runtime of O(1)
   inserting into the list at a random location would be O(n) for iteration

2. What is the runtime complexity of `ListNode.insert_before`?
   insertion runtime of O(1)
   inserting into the list at a random location would be O(n) for iteration

3. What is the runtime complexity of `ListNode.delete`?
   assignment to bypass deleted node
   runtime of O(1)

4. What is the runtime complexity of `DoublyLinkedList.add_to_head`?
   reference head and insert new node
   runtime of O(1)

5. What is the runtime complexity of `DoublyLinkedList.remove_from_head`?
   reference head and remove, reassign next node as head
   runtime of O(1)

6. What is the runtime complexity of `DoublyLinkedList.add_to_tail`?
   reference tail, add to end, reassign tail
   runtime of O(1)

7. What is the runtime complexity of `DoublyLinkedList.remove_from_tail`?
   reference tail, remove node, reassign tail
   runtime of O(1)

8. What is the runtime complexity of `DoublyLinkedList.move_to_front`?
   add incoming node to head, then reassign next and previous on the incoming effectively deleting it
   runtime of O(1)

9. What is the runtime complexity of `DoublyLinkedList.move_to_end`?
   add incoming node to tail, then reassign next and previous on the incoming effectively deleting it
   runtime of O(1)

10. What is the runtime complexity of `DoublyLinkedList.delete`?
    running remove from tail or remove from head, or running delete on the node
    runtime of O(1)

    a. Compare the runtime of the doubly linked list's `delete` method with the worst-case runtime of the JS `Array.splice` method. Which method generally performs better?
    selected elements from an array are removed from array, leaving a gap in the array, all elements to the right need to be shifted up to fill the gap.
    worst case runtime of O(n)
