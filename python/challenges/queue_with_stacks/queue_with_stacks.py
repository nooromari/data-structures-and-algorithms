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
        list_data = ""
        current = self.top
        while current:
            list_data += f"{current.value} -> "
            current = current.next
        list_data += "NULL"
        return list_data


class PseudoQueue:
    def __init__(self):
        self.queue_front = Stack()
        self.queue_rear = Stack()

    def enqueue(self, value):
        """
        inserts value into the PseudoQueue, using a first-in, first-out approach.
        """
        self.queue_front.push(value)

    def dequeue(self):
        """
        extracts a value from the PseudoQueue, using a first-in, first-out approach.
        """
        if not self.queue_rear.top and not self.queue_front.top:
            return "queue is empty"

        while self.queue_front.top:
            self.queue_rear.push(self.queue_front.pop())
        final = self.queue_rear.pop()

        while self.queue_rear.top:
            temp_top = self.queue_rear.pop()
            self.queue_front.push(temp_top)
        return final

    def __str__(self):
        """ Returns a string representaiton of the linked list
            1 -> 3 -> 4 -> Null
        """
        list_data = ""
        current = self.queue_front.top
        while current:
            list_data += f"{current.value} -> "
            current = current.next
        list_data += "NULL"
        return list_data


if __name__ == "__main__":
    queue = PseudoQueue()
    queue.enqueue(5)
    queue.enqueue(9)
    print('**',queue)
    print('del',queue.dequeue())
    print('****',queue)
