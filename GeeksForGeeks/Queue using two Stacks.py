# User function Template for python3

# Function to push an element in queue by using 2 stacks.
def Push(x, stack1, stack2):
    '''
    x: value to push
    stack1: list
    stack2: list
    '''
    # code here

    stack1.append(x)


# Function to pop an element from queue by using 2 stacks.
def Pop(stack1, stack2):
    '''
    stack1: list
    stack2: list
    '''
    # code here
    if len(stack2) != 0:
        popped = stack2.pop()
        return popped
    else:
        while len(stack1) > 0:
            popped = stack1.pop()
            stack2.append(popped)
        if len(stack2) == 0:
            return -1
        popped = stack2.pop()
        return popped
