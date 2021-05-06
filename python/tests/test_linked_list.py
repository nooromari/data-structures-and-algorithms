import pytest
from linked_list.linked_list import *


def test_insert(list_test):
    excpected = "{ 10 } -> { 1 } -> { 0 } -> { None } -> NULL"
    actual = f"{list_test}"
    assert excpected == actual

def test_includes(list_test):
    inputs = [55,"Manar",10]
    actual = [list_test.includes(ele) for ele in inputs]
    excpected = [False, False , True]
    assert excpected == actual


@pytest.fixture
def list_test():
    linked = Linked_list()
    linked.insert()
    linked.insert(0)
    linked.insert(1)
    linked.insert(10)
    return linked

