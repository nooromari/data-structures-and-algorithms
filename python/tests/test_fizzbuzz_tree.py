from challenges.fizzbuzz_tree.fizzbuzz_tree import *
import pytest

def test_k_array(tree_test):
    k_tree = K_ary_tree(tree_test)
    actual = FizzBuzzTree(k_tree)
    expected = ['Buzz', 'Buzz', '2', 'Fizz', '7', '2', '4', 'FizzBuzz', 'Fizz', '1']
    assert actual == expected


def test_not_int_tree(tree_not_int):
    k_tree = K_ary_tree(tree_not_int)
    actual = FizzBuzzTree(k_tree)
    expected = 'the value should be an integer'
    assert actual == expected


@pytest.fixture
def tree_test():
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
    return node

@pytest.fixture
def tree_not_int():
    node = KNode('10')
    node.children.append(KNode('k'))
    node.children.append(KNode(2))
    return node