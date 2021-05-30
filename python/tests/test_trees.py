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
#   print(sb.contains(3),sb.contains(13))
#   print(sb.in_order())