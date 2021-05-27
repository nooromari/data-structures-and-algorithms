class Queue:
  def __init__(self):
    self.front = None
    self.rear = None

class TNode:
  def __init__(self, value=None):
    self.value = value
    self.left = None
    self.right = None

class BinaryTree:
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



if __name__ == "__main__":
  node1 = TNode(1)
  node1.left = TNode(2)
  node1.right = TNode(3)
  node1.right.left = TNode(4)
  node1.right.right = TNode(5)

  binary_tree = BinaryTree(node1)



  print(binary_tree.pre_order())
#   binary_tree.pre_order_iter()
  print("-"*20)
  print(binary_tree.in_order())

  print("-"*20)
  print(binary_tree.post_order())