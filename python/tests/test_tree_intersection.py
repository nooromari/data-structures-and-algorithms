from challenges.tree_intersection.tree_intersection import tree_intersection
from Data_Structures.tree.tree import *

import pytest

def test_tree_intersection(tree1,tree2):
    """
    test if return the common values for 2 trees have the same structure.
    """
    actual = tree_intersection(tree1, tree2)
    expected = [125, 325]
    assert actual == expected

    
def test_tree_intersection2(tree1,tree3):
    """
    test if return an empty array for 2 trees don't have a common value.
    """
    actual = tree_intersection(tree1, tree3)
    expected = []
    assert actual == expected
    

def test_tree_intersection3(tree2,tree3):
    """
    test if return the common values for 2 trees don't have the same structure.
    """
    actual = tree_intersection(tree2, tree3)
    expected = [10, -75]
    assert actual == expected


@pytest.fixture
def tree1():
  node = TNode(100)
  node.left = TNode(125)
  node.right = TNode(325)
  node.right.left = TNode(4)
  node.right.right = TNode(75)
  binary_tree = Binary_tree(node)
  return binary_tree

@pytest.fixture
def tree2():
  node = TNode(10)
  node.left = TNode(125)
  node.right = TNode(325)
  node.right.left = TNode(9)
  node.right.right = TNode(-75)
  binary_tree = Binary_tree(node)
  return binary_tree

@pytest.fixture
def tree3():
  node = TNode(10)
  node.left = TNode(0)
  node.right = TNode('7')
  node.right.right = TNode(-75)
  binary_tree = Binary_tree(node)
  return binary_tree

