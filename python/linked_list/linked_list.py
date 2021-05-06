# Define Node
class Node:
  def __init__(self, data=None):
      self.data = data
      self.next = None
  # use a magic method so when you print node you see it's value
  
  def __str__(self):
      return f"{self.data}"

# Define linked list
class Linked_list:
  # Constructor
  def __init__(self):
    self.head = None
  # define your append method
  def insert (self, data=None):
    new_node = Node(data)
    # Once we have a head 
    if self.head :
      new_node.next = self.head # set our current pointer to the head
      #Assign new_node to self.head 
    self.head = new_node
      # while there is a following node that's not None

  def includes(self,value):
    current = self.head 
    is_include = False
    while (current):
        if current.data == value :
            is_include = True
        current = current.next
    return is_include
      

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
      list_data += "{ %s } -> " %(current.data,)
      # step 2b:  move to the next item
      current = current.next
    list_data += "NULL"
    # step 3 - return the final string
    return list_data
  


# Write program here
if __name__ == "__main__":
  linked = Linked_list()
  linked.insert()
  linked.insert("Muhannad")
  linked.insert("Manar")
  linked.insert(10)
  print(linked)
  print(linked.includes(55),linked.includes("Manar"),linked.includes(10))

# I am finally here