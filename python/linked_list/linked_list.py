# Define Node
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
    # use a magic method so when you print node you see it's value

    def __str__(self):
        return f"{self.data}"


# Define linked list
class LinkedList:
    # Constructor
    def __init__(self):
        self.head = None
    # define your append method

    def insert(self, data=None):
        """
        takes any value as an argument and adds a new node with that value to the head of the list 
        """
        new_node = Node(data)
        # Once we have a head
        if self.head:
            new_node.next = self.head  # set our current pointer to the head
            # Assign new_node to self.head
        self.head = new_node
        # while there is a following node that's not None

    def includes(self, value):
        """
        takes any value as an argument and returns a boolean result depending on whether that value exists as a Node’s value somewhere within the list.
        """
        current = self.head
        is_include = False
        while (current):
            if current.data == value:
                is_include = True
            current = current.next
        return is_include

    def append(self, data):
        """
        adds a new node with the given value to the end of the list
        """
        new_data = Node(data)
        current = self.head
        if self.head:
            while(current.next):
                current = current.next
            current.next = new_data
        else:
            self.head = new_data

    def insertAfter(self, data, new_data):
        """
        add a new node with the given newValue immediately before the first value node
        """
        try:
          if self.includes(data):
              new_node = Node(new_data)
              current = self.head
              while (current):
                  if current.data == data:
                      new_node.next = current.next
                      current.next = new_node
                      break
                  current = current.next
        except:
          raise Exception("the value not found in the list")

    def insertBefore(self, data, new_data):
        """
        add a new node with the given newValue immediately after the first value node
        """
        try:
            if self.includes(data):
                new_node = Node(new_data)
                current = self.head
                if current.data == data:
                    new_node.next = self.head
                    self.head = new_node
                else:
                    while (current.next):
                        if current.next.data == data:
                            new_node.next = current.next
                            current.next = new_node
                            break
                        current = current.next
        except:
          raise Exception("the value not found in the list")

    def __str__(self):
        """ Returns a string representaiton of the linked list
            1 -> 3 -> 4 -> Null
        """
        # step 0 - create a new empty string
        list_data = ""
        # step 1 iterate over each node
        current = self.head
        while current:
            # step 2 - insert each data to the string
            list_data += f"{current.data} -> "
            # step 2b:  move to the next item
            current = current.next
        list_data += "NULL"
        # step 3 - return the final string
        return list_data


# Write program here
if __name__ == "__main__":
    linked = LinkedList()
    # linked.insert()
    # linked.insert("Muhannad")
    # linked.insert("Manar")
    # linked.insert(10)
    # linked.insert(6)
    linked.append(1)
    linked.append(3)
    linked.append(2)
    linked.insertAfter(3, 10)
    linked.insertBefore(100, 7)
    linked.insertAfter(25,20)
    print(linked)
    # print(linked.includes(55),linked.includes("Manar"),linked.includes(10))

# I am finally here
