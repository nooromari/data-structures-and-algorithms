class EmptyStackException(Exception):
    pass

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class Stack(Node):
    def __init__(self):
        self.top = None

    def push(self, value):
        """ Add an item to the top fo the stack """
        if not self.top:
            self.top = Node(value)
        else:
            node = Node(value)
            node.next = self.top
            self.top = node

    def pop(self):
        """ Removes the node from the top of the stack, and returns the node’s value. """
        try:
            temp = self.top
            self.top = self.top.next
            temp.next = None
            return temp.value
        except Exception:
            return "the stack is empty"

    def is_empty(self):
        """ Returns True if Empty and False otherwise """
        if self.top:
            return False
        return True

    def peek(self):
        """ Returns the value at the top without modifying the stack, raises an exception otherwise """
        try:
            return self.top.value
        except Exception:
            return "the stack is empty"

    def __str__(self):
        """ Returns a string representaiton of the linked list
            1 -> 3 -> 4 -> Null
        """
        # step 0 - create a new empty string
        list_data = ""
        # step 1 iterate over each node
        current = self.top
        while current:
            # step 2 - insert each data to the string
            list_data += f"{current.value} -> "
            # step 2b:  move to the next item
            current = current.next
        list_data += "NULL"
        # step 3 - return the final string
        return list_data


class Queue(Node):
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        """ Add an item to the rear fo the queue """
        node = Node(value)

        if not self.front:
            # we have an emtpy queue
            self.front = node
            self.rear = node
        else:
            # make sure the previous rear will now point to the new node
            self.rear.next = node
            # move our rear to point to the new node
            self.rear = self.rear.next

    def dequeue(self):
        """ removed an item to the front fo the queue """
        try:
            temp = self.front
            self.front = self.front.next
            temp.next = None
            return temp.value
        except Exception:
            return "the queue is empty"
        

    def is_empty(self):
        """ Returns True if Empty and false otherwise """
        if self.front:
            return False
        return True

    def peek(self):
        """ Returns the value at the front without modifying the stack, raises an exception otherwise """
        try:
            return self.front.value
        except Exception:
            return "the queue is empty"

    def __str__(self):
        """ Returns a string representaiton of the linked list
            1 -> 3 -> 4 -> Null
        """
        # step 0 - create a new empty string
        list_data = ""
        # step 1 iterate over each node
        current = self.front
        while current:
            # step 2 - insert each data to the string
            list_data += f"{current.value} -> "
            # step 2b:  move to the next item
            current = current.next
        list_data += "NULL"
        # step 3 - return the final string
        return list_data


if __name__ == "__main__":
    stack = Stack()
    stack.push(0)
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack)
    queue = Queue()
    print(queue)


