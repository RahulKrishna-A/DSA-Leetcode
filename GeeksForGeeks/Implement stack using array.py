# User function Template for python3

class MyStack:

    def __init__(self):
        self.arr = []

    # Function to push an integer into the stack.
    def push(self, data):
        # add code here
        self.arr.append(data)
        return

    # Function to remove an item from top of the stack.
    def pop(self):
        # add code here
        if len(self.arr) == 0:
            return -1
        else:
            ele = self.arr.pop()
            return ele

