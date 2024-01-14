# User function Template for python3

# design the class in the most optimal way

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LRUCache:

    # Constructor for initializing the cache capacity with the given value.
    def __init__(self, cap):
        # code here
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.memo = {}
        self.cap = cap

    # Function to return value corresponding to the key.
    def get(self, key):
        # code here
        if key in self.memo:
            value = self.memo[key].data[1]
            node = self.memo[key]
            node.prev.next = node.next
            node.next.prev = node.prev

            node.next = self.head.next
            node.prev = self.head.next.prev
            self.head.next.prev = node
            self.head.next = node
            return value
        return -1

    # Function for storing key-value pair.
    def set(self, key, value):
        # code here
        # if len(self.memo)>=self.cap:
        #     del self.memo[self.tail.prev.data[0]]
        #     self.tail.prev.prev.next = self.tail
        #     self.tail.prev = self.tail.prev.prev

        # if key in self.memo:
        #     self.memo[key].data = [key,value]
        #     node = self.memo[key]
        #     node.prev.next = node.next
        #     node.next.prev = node.prev

        #     node.next = self.head.next
        #     node.prev = self.head.next.prev
        #     self.head.next.prev = node
        #     self.head.next = node

        # else:
        #     node = Node([key,value])
        #     self.memo[key] = node
        #     node.next = self.head.next
        #     node.prev = self.head.next.prev
        #     self.head.next.prev = node
        #     self.head.next = node
        #     self.memo[key]=node

        if key in self.memo:
            node = self.memo[key]
            node.data = [key, value]

            # Move the updated node to the front of the linked list.
            node.prev.next = node.next
            node.next.prev = node.prev
            node.next = self.head.next
            node.prev = self.head.next.prev
            self.head.next.prev = node
            self.head.next = node

        else:
            # If the cache is full, remove the least recently used entry.
            if len(self.memo) >= self.cap:
                del self.memo[self.tail.prev.data[0]]
                self.tail.prev.prev.next = self.tail
                self.tail.prev = self.tail.prev.prev

            # Create a new node and add it to the front of the linked list.
            node = Node([key, value])
            self.memo[key] = node
            node.next = self.head.next
            node.prev = self.head.next.prev
            self.head.next.prev = node
            self.head.next = node

