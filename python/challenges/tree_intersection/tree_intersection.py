from Data_Structures.tree.tree import *
from Data_Structures.hashtable.hashtable import Hashmap

def tree_intersection(tree1,tree2):
    """
    takes two binary tree parameters and return a set of values found in both trees.
    """
    tree_hash = add_tree_to_hashmap(tree1)

    new_list = []
    def add_common_to_list(node):
        str_value = str(node.value)
        if tree_hash.contains(str_value):
            new_list.append(node.value)

        if node.left:
            add_common_to_list(node.left)

        if node.right:
            add_common_to_list(node.right)

    if tree2.root:
        add_common_to_list(tree2.root)
    return new_list


def add_tree_to_hashmap(tree):
    hashmap = Hashmap()
    def walk(node):
        str_value = str(node.value)
        hashmap.add(str_value, 1)

        if node.left:
            walk(node.left)

        if node.right:
            walk(node.right)

    if tree.root:
        walk(tree.root)
    return hashmap
        
