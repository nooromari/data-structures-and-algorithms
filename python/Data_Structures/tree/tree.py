# from Data_Structures.stackes_and_queue.stackes_and_queue import Queue

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        """ Add an item to the rear fo the queue """
        node = Node(value)

        if not self.front:

            self.front = node
            self.rear = node
        else:
            self.rear.next = node
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

class TNode:
  def __init__(self, value=None):
    self.value = value
    self.left = None
    self.right = None

class Binary_tree:
  def __init__(self, root=None):
    self.root = root
    self.pre_values = []
    self.in_values = []
    self.post_values = []

  def pre_order(self):
    """ Pre-order traversal of our tree """
    def walk(root):
      self.pre_values.append(root.value)

      if root.left:
        walk(root.left)
      
      if root.right:
        walk(root.right)
         
    walk(self.root)
    return self.pre_values

  def in_order(self):
    """ Pre-order traversal of our tree """
    def walk(root):

      if root.left:
        walk(root.left)

      self.in_values.append(root.value)

      if root.right:
        walk(root.right)
         
    walk(self.root)
    return self.in_values
  
  def post_order(self):
    """ Pre-order traversal of our tree """
    def walk(root):

      if root.left:
        walk(root.left)

      if root.right:
        walk(root.right)

      self.post_values.append(root.value)
   
    walk(self.root)
    return self.post_values

  def find_maximum_value(self):
    """return the maximum value stored in the tree"""
    if self.root: 
      self.max_val = self.root.value
    else:
      return 'No tree found'
    def inner(root):
      if root.left:
        inner(root.left)

      if root.right:
        inner(root.right)

      if self.max_val < root.value:
        self.max_val = root.value

    inner(self.root)
    return self.max_val

  def breadth_first(self):
    """traverse the input tree using a Breadth-first approach, and return a list of the values in the tree in the order """
    self.breadth_first_list = []
    queque = Queue()
    queque.enqueue(self.root)
    while not queque.is_empty():
      ele = queque.dequeue()
      self.breadth_first_list.append(ele.value)
      if ele.left is not None:
        queque.enqueue(ele.left)
      if ele.right is not None:
        queque.enqueue(ele.right)
    return self.breadth_first_list

  def binaryTreePaths(self):
    """
    return all tha paths for a binary tree
    """
    self.paths = []
    self.path = []
        
    def walk(node):
        if node:
          self.path.append(node.value)

          if (not node.left) and (not node.right):
            p = self.path.copy()
            self.paths.append(p)

          if node.left:
            walk(node.left)
  
          if node.right:
            walk(node.right)
          self.path.pop() 
            
    walk(self.root)
    return self.paths

  def binaryTreeShortestPath(self):
    """
    return tha shortest path for a binary tree
    """
    paths = self.binaryTreePaths()
    shortest = paths[0]
    for path in paths :
      if len(path) < len(shortest):
        shortest = path
    return shortest
    
class Binary_search_tree:
  
  def __init__(self,value=None):
    self.node = TNode(value)

  def add(self,value):
    if (self.node.value == None):
      self.node.value = value
    else:
      if value == self.node.value: 
        return 'no duplicates aloowed in binary search self'
      if (value < self.node.value):
        if(self.node.left):
          self.node.left.add(value)
        else: 
          self.node.left = Binary_search_tree(value)
      else:
        if(self.node.right):
          self.node.right.add(value)
        else: 
          self.node.right = Binary_search_tree(value)

  def in_order(self, lst = []):
    if (self.node.left):
        self.node.left.in_order(lst)
    lst.append(self.node.value)
    if (self.node.right):
        self.node.right.in_order(lst)
    return lst

  def contains(self,value,parent= None):
    """check if the value inside the tree"""
    if value == self.node.value: 
      return True
    if (value < self.node.value):
      if (self.node.left):
        return self.node.left.contains(value, self.node)
      else: 
        return False
    else:
      if (self.node.right):
        return self.node.right.contains(value, self.node)
      else:
        return False


if __name__ == "__main__":
  node1 = TNode(2)
  node1.left = TNode(7)
  node1.right = TNode(5)
  node1.right.left = TNode(4)
  node1.left.left = TNode(2)
  node1.left.right = TNode(6)
  node1.left.left.left = TNode(5)
  node1.left.right.right = TNode(11)
  node1.right.right = TNode(9)
  # node1.right.right.left = TNode(4)
  binary_tree = Binary_tree(node1)
  # print(binary_tree.pre_order())
  # print("-"*20)
  # print(binary_tree.in_order())

  # print("-"*20)
  # print(binary_tree.post_order())

  # print(binary_tree.find_maximum_value())
  # print(binary_tree.breadth_first())

  print(binary_tree.binaryTreePaths())
  print(binary_tree.binaryTreeShortestPath())


  sb = Binary_search_tree()
  sb.add(5)
  sb.add(4)
  sb.add(3)
  sb.add(1)
  sb.add(2)
  sb.add(6)
  sb.add(100)
  sb.add(0)
  # print(sb.contains(3),sb.contains(13))
  # print(sb.in_order())