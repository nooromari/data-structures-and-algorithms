
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

class KNode:
  def __init__(self, value=None):
    self.value = value
    self.children = [] 

class K_ary_tree:
    def __init__(self, root=None):
        self.root = root

    def breadth_first(self):
        self.breadth_first_list = []
        queque = Queue()
        queque.enqueue(self.root)
        while not queque.is_empty():
            ele = queque.dequeue()
            self.breadth_first_list.append(ele.value)
            if ele.children :
                for i in ele.children:
                    queque.enqueue(i)
        return self.breadth_first_list

    
def FizzBuzzTree(tree):
    fizzbuzzlist = []
    queque = Queue()
    queque.enqueue(tree.root)
    while not queque.is_empty():
        item = queque.dequeue()
        try:
            if item.value % 15 == 0:
                item.value = "FizzBuzz"
            elif item.value % 3 ==0 :
                item.value = 'Fizz'
            elif item.value % 5 ==0:
                item.value = 'Buzz'
            else :
                item.value = str(item.value)
            fizzbuzzlist.append(item.value)
            if len(item.children) > 0 :
                for i in item.children:
                    queque.enqueue(i)
        except TypeError:
            return 'the value should be an integer'
    return fizzbuzzlist


if __name__ == '__main__':
    node = KNode(10)
    node.children.append(KNode(5))
    node.children.append(KNode(2))
    node.children.append(KNode(3))
    node.children[0].children.append(KNode(7))
    node.children[1].children.append(KNode(2))
    node.children[1].children.append(KNode(4))
    node.children[2].children.append(KNode(30))
    node.children[2].children.append(KNode(6))
    node.children[2].children.append(KNode(1))

    k_tree = K_ary_tree(node)
    print(k_tree.breadth_first())
    print(FizzBuzzTree(k_tree))
