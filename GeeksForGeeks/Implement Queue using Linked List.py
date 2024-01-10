# A linked list (LL) node
# to store a queue entry
'''class Node:

    def __init__(self, data):
        self.data = data
        self.next = None'''


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class MyQueue:
    head = None
    tail = None

    # Function to push an element into the queue.
    def push(self, item):
        if self.head == None:
            self.head = Node(item)
            self.tail = self.head
        else:
            self.tail.next = Node(item)
            self.tail = self.tail.next

        # Add code here

    # Function to pop front element from the queue.
    def pop(self):
        if self.head == None:
            return -1
        popped = self.head.data
        self.head = self.head.next
        return popped

