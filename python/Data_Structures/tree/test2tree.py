# # import pysnooper

# class Node:
#   def __init__(self, value):
#     self.value = value
#     self.next = None

# class Stack:
#   def __init__(self, node=None):
#     self.top = node
  
#   def push(self, value):
#     if not self.top:
#         self.top = Node(value)
#     else:
#         node = Node(value)
#         node.next = self.top
#         self.top = node

#   def pop(self):
#     if not self.is_empty():
#       temp_node = self.top
#       self.top = self.top.next
#       temp_node.next = None
#       return temp_node.value
#     raise Exception("Cannot pop an empty Stack")
  
#   def is_empty(self):
#     return not self.top

# class Queue:
#   def __init__(self):
#     self.front = None
#     self.rear = None

# class TNode:
#   def __init__(self, value=None):
#     self.value = value
#     self.left = None
#     self.right = None

# class BinaryTree:
#     def __init__(self, root=None):
#         self.root = root

#     def pre_order(self):
#         """ Pre-order traversal of our tree """
#         pre_values = []
#         def walk(root):
#             pre_values.append(root.value)

#             if root.left:
#                 walk(root.left)
            
#             if root.right:
#                 walk(root.right)
            
#         walk(self.root)
#         return pre_values

#     def in_order(self):
#         """ in-order traversal of our tree """
#         in_values = []
#         def walk(root):
#             if root.left:
#                 walk(root.left)
        
#             self.in_values.append(root.value)

#             if root.right:
#                 walk(root.right)
            
#         walk(self.root)
#         return f'{in_values}'

    
#     # @pysnooper.snoop()
#     def post_order(self):
#         """ post-order traversal of our tree """
#         post_values = []
#         def walk(root):
#             if root.left:
#                 walk(root.left)
        
#             if root.right:
#                 walk(root.right)
#             post_values.append(root.value)
            
#         walk(self.root)
#         return post_values
        
  

# class BinaryTree:
#   def __init__(self, root=None):
#     self.root = root
#     self.children = []

#   def pre_order(self):
#     """ Pre-order traversal of our tree """
#     def walk(root):
#       self.children.append(root.value)

#       if root.left:
#         walk(root.left)
      
#       if root.right:
#         walk(root.right)
         
#     walk(self.root)
#     return ' '.join(f"{self.children}")


#   def in_order(self):
#     """ Pre-order traversal of our tree """
#     def walk(root):

#       if root.left:
#         walk(root.left)

#       self.children.append(root.value)

#       if root.right:
#         walk(root.right)
         
#     walk(self.root)
#     return ' '.join(f"{self.children}")
  
#   def post_order(self):
#     """ Pre-order traversal of our tree """
#     def walk(root):

#       if root.left:
#         walk(root.left)


#       if root.right:
#         walk(root.right)

#       self.children.append(root.value)
   
#     walk(self.root)
#     return ' '.join(f"{self.children}")



# if __name__ == "__main__":
#   node1 = TNode(1)
#   node1.left = TNode(2)
#   node1.right = TNode(3)
#   node1.right.left = TNode(4)
#   node1.right.right = TNode(5)


#   binary_tree = BinaryTree(node1)

#   print(binary_tree.pre_order())
#   print(binary_tree.in_order())
#   print(binary_tree.post_order())

   



# # Think about
# class KNode:
#   def __init__(self, value=None):
#     self.value = value
#     # How could you implement this for k of any size?
#     self.children = []



# class Node:
#   def __init__(self, value):
#     self.value = value
#     self.next = None

# class Stack:
#   def __init__(self, node=None):
#     self.top = node
  
#   def push(self, value):
#     if not self.top:
#         self.top = Node(value)
#     else:
#         node = Node(value)
#         node.next = self.top
#         self.top = node

#   def pop(self):
#     if not self.is_empty():
#       temp_node = self.top
#       self.top = self.top.next
#       temp_node.next = None
#       return temp_node.value
#     raise Exception("Cannot pop an empty Stack")
  
#   def is_empty(self):
#     return not self.top

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

class Binary_search_tree:
    def __init__(self,root=None):
        self.root = root
        self.left = None
        self.right = None
        self.pre_values = []

    def add(self,val):
        # check if there is no root
        if (self.root == None):
            self.root = val
        # check where to insert
        else:
            # check for duplicate then stop and return
            if val == self.root: return 'no duplicates aloowed in binary search tree'
            # check if value to be inserted < currentNode's value
            if (val < self.root):
                # check if there is a left node to currentNode if true then recurse
                if(self.left):
                    self.left.insert(val)
                # insert where left of currentNode when currentNode.left=None
                else: self.left = Binary_search_tree(val)

            # same steps as above here the condition we check is value to be inserted > currentNode's value
            else:
                if(self.right):
                    self.right.add(val)
                else: self.right = Binary_search_tree(val)

    def contains(self,key):
        """accepts a value, and returns a boolean indicating whether or not the value is in the tree at least once."""
        # Base Cases: root is null or key is present at root
        if self is None or self.root == key:
            return self

        # Key is greater than root's key
        if self.root < key:
            return self.contains(self.right,key)

        # Key is smaller than root's key
        return self.contains(self.left,key)

    def pre_order(self, lst):
        lst.append(self.val)
        if (self.left):
            self.left.pre_order(lst)
        if (self.right):
            self.right.pre_order(lst)
        return lst
    

    
    

# class Binary_search_tree:
#     def __init__(self, root=None):
#         self.root = root
#         self.pre_values = []

#     # def add(self,val):
#     #     """ accepts a value, and adds a new node with that value in the correct location in the binary search tree."""
#     #     current = self.root
#     #     new_node = TNode(val)
#     #     if self.root is None:
#     #         self.root = new_node

#     #     if current.value < val:
#     #         if current.right is None:
#     #             current.right = new_node
#     #         else:
#     #             current = current.right

#     #     elif current.value > val:
#     #         if current.left is None:
#     #             current.left = new_node


#     def add(self, val):
#         """ accepts a value, and adds a new node with that value in the correct location in the binary search tree."""
#         def insert(root, key):
#             if root is None:
#                 root = TNode(key)
#             else:
#                 if root.value == key:
#                     return root
#                 elif root.value < key:
#                     root.right = insert(root.right, key)
#                 else:
#                     root.left = insert(root.left, key)
#             return root
#         insert(self.root, val)
#         # current = self
#         # # new_node = TNode(val)
#         # if not current.root:
#         #     self.root = TNode(val)
#         #     return 

#         # if current.root.value == val:
#         #     return 
            
#         # if val < current.root.value:
#         #     print('in', current.root.value,val)
#         #     if current.root.left:
#         #         print('inin', current.root.value,val)
#         #         Binary_search_tree.add(self,val)
#         #         return 
#         #     current.root.left = TNode(val)
#         #     return

#         # if val > current.root.value:
#         #     if current.root.right:
#         #         Binary_search_tree.add(self,val)
#         #         return current.root
#         #     current.root.right = TNode(val)

    # def pre_order(self):
    #     """ Pre-order traversal of our tree """
    #     def walk(root):
    #         self.pre_values.append(root.value)

    #         if root.left:
    #             walk(root.left)
            
    #         if root.right:
    #             walk(root.right)
                
    #     walk(self.root)
    #     return self.pre_values

 
#     # A utility function to search a given key in BST
#     def contains(self,key):
#         """accepts a value, and returns a boolean indicating whether or not the value is in the tree at least once."""
        
#         # Base Cases: root is null or key is present at root
#         if self is None or self.root == key:
#             return self
    
#         # Key is greater than root's key
#         if self.root < key:
#             return self.contains(self.right,key)
    
#         # Key is smaller than root's key
#         return self.contains(self.left,key)
    
    # This code is contributed by Bhavya Jain


#   def pre_order_iter(self):
#     stack = Stack()
#     stack.push(self.root)

#     while not stack.is_empty():
#       item = stack.pop()
#       print(item.value)

#       if item.right is not None:
#         stack.push(item.right)

#       if item.left is not None:
#         stack.push(item.left)
  
#   def bread_first(self):
#      # Use queque for FIFO
#      pass



if __name__ == "__main__":
  node1 = TNode(1)
  node1.left = TNode(2)
  node1.right = TNode(3)
  node1.right.left = TNode(4)
  node1.right.right = TNode(5)

  binary_tree = BinaryTree(node1)
  sbt = Binary_search_tree()
  sbt.add(3)
  sbt.add(2)
  sbt.add(4)
  sbt.add(5)
  print(sbt.pre_order())


#   print(binary_tree.pre_order())
# #   binary_tree.pre_order_iter()
#   print("-"*20)
#   print(binary_tree.in_order())

#   print("-"*20)
#   print(binary_tree.post_order())


# Think about
class KNode:
  def __init__(self, value=None):
    self.value = value
    # How could you implement this for k of any size?
    self.children = []


    # def add(self, key):
    #     def add_r(root,key):
    #         if root is None:
    #             root = TNode(key)
    #         else:
    #             if root.value == key:
    #                 root.right = TNode(key)
    #             elif root.value < key:
    #                 root.right = add_r(root.right, key)
    #             else:
    #                 root.left = add_r(root.left, key)
    #         return root
    #     add_r(self.root,key)

        # def add(self, value):
    #     if not self.root:
    #         self.root = value
    #         return self.root

    #     if self.root == value:
    #         return self.root

    #     if value < self.root:
    #         if self.root.left:
    #             self.left.add(value)
    #             return self.root
    #         self.root.left = TNode(value)
    #         return self.root

    #     if self.root.right:
    #         self.root.right.add(value)
    #         return self.root
    #     self.root.right = TNode(value)