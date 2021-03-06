from Data_Structures.tree.tree import *
import pytest


def test_binary_tree(binary_tree):
    actual = [binary_tree.pre_order(), binary_tree.in_order(), binary_tree.post_order()]
    expected = [[1, 2, 3, 4, 5], [2, 1, 4, 3, 5], [2, 4, 5, 3, 1]]
    assert actual == expected

def test_binary_search_tree(binary_search_tree):
    actual = binary_search_tree.in_order()
    expected = [0, 1, 2, 3, 4, 5, 6, 100]
    assert actual == expected
    actual = [binary_search_tree.contains(3), binary_search_tree.contains(13)]
    expected = [True, False]
    assert actual == expected

def test_find_maximum_value(binary_tree):
    actual = binary_tree.find_maximum_value()
    expected = 5
    assert actual == expected

def test_breadth_first(breadth_test_tree):
  actual = breadth_test_tree.breadth_first()
  expected = [2, 7, 5, 2, 6, 9, 5, 11, 4]
  assert actual == expected


@pytest.fixture
def binary_tree():
  node = TNode(1)
  node.left = TNode(2)
  node.right = TNode(3)
  node.right.left = TNode(4)
  node.right.right = TNode(5)
  binary_tree = Binary_tree(node)
  return binary_tree


@pytest.fixture
def binary_search_tree():
  bst = Binary_search_tree()
  bst.add(5)
  bst.add(4)
  bst.add(3)
  bst.add(1)
  bst.add(2)
  bst.add(6)
  bst.add(100)
  bst.add(0)
  return bst

@pytest.fixture
def breadth_test_tree():
  node1 = TNode(2)
  node1.left = TNode(7)
  node1.right = TNode(5)
  node1.left.left = TNode(2)
  node1.left.right = TNode(6)
  node1.left.left.left = TNode(5)
  node1.left.right.right = TNode(11)
  node1.right.right = TNode(9)
  node1.right.right.left = TNode(4)
  binary_tree = Binary_tree(node1)
  return binary_tree