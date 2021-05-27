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

class Binary_search_tree:
    def __init__(self,value=None):
      self.node = TNode(value)
    def add(self,value):
        if (self.node.value == None):
            self.node.value = value
        else:
            if value == self.node.value: return 'no duplicates aloowed in binary search self'
            if (value < self.node.value):
                if(self.node.left):
                    self.node.left.add(value)
                else: self.node.left = Binary_search_tree(value)
            else:
                if(self.node.right):
                    self.node.right.add(value)
                else: self.node.right = Binary_search_tree(value)


    def in_order(self, lst = []):
        if (self.node.left):
            self.node.left.in_order(lst)
        lst.append(self.node.value)
        if (self.node.right):
            self.node.right.in_order(lst)
        return lst

    def contains(self,value,parent= None):
        if value == self.node.value: return True
        if (value < self.node.value):
            if (self.node.left):
                return self.node.left.contains(value, self.node)
            else: return False
        else:
            if (self.node.right):
                return  self.node.right.contains(value, self.node)
            else: return False


if __name__ == "__main__":
  node1 = TNode(1)
  node1.left = TNode(2)
  node1.right = TNode(3)
  node1.right.left = TNode(4)
  node1.right.right = TNode(5)
  binary_tree = Binary_tree(node1)
  print(binary_tree.pre_order())
  print("-"*20)
  print(binary_tree.in_order())

  print("-"*20)
  print(binary_tree.post_order())

  sb = Binary_search_tree()
  sb.add(5)
  sb.add(4)
  sb.add(3)
  sb.add(1)
  sb.add(2)
  sb.add(6)
  sb.add(100)
  sb.add(0)
  print(sb.contains(3),sb.contains(13))
  print(sb.in_order())