

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class Stack:
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



class Pseudo_Queue(Stack):

    def __init__(self):
        super().__init__()
        self.enqueue_front = Stack()
        self.dequeue_rear = Stack()
        # self.front = None
        # self.rear = None

    def enqueue(self, value):
        """
         inserts value into the PseudoQueue, using a first-in, first-out approach.
        """
        self.enqueue_front.push(value)
        # self.front = Node(self.enqueue_front.peek())

    def dequeue(self):
        """
        extracts a value from the PseudoQueue, using a first-in, first-out approach.
        """
        pass

    def __str__(self):
        super().__str__()
    #     """ Returns a string representaiton of the linked list
    #         1 -> 3 -> 4 -> Null
    #     """
    #     # step 0 - create a new empty string
    #     list_data = ""
    #     # step 1 iterate over each node
    #     current = self.top
    #     while current:
    #         # step 2 - insert each data to the string
    #         list_data += f"{current.value} -> "
    #         # step 2b:  move to the next item
    #         current = current.next
    #     list_data += "NULL"
    #     # step 3 - return the final string
    #     return list_data



if __name__ =="__main__":
    queue = Pseudo_Queue()
    queue.enqueue(5)
    queue.enqueue(9)
    queue.enqueue(5)
    queue.enqueue(9)
    print(queue)
