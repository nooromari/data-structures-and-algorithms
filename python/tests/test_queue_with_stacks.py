import pytest

from challenges.queue_with_stacks.queue_with_stacks import *


def test_Pseudo_Queue(queue_test):
    actual = f"{queue_test}"
    expected = "2 -> 1 -> 0 -> NULL"
    assert actual == expected

def test_queue_dequeue(queue_test):
    actual = queue_test.dequeue()
    expected = 0
    assert actual == expected
    actual = f"{queue_test}"
    expected ='2 -> 1 -> NULL'
    assert actual == expected
    queue_test.dequeue()
    queue_test.dequeue()
    actual = queue_test.dequeue()
    expected = 'queue is empty'
    assert actual == expected   

  

@pytest.fixture
def queue():
    return PseudoQueue()

@pytest.fixture
def queue_test(queue):
    queue.enqueue(0)
    queue.enqueue(1)
    queue.enqueue(2)
    return queue

