import pytest
from Data_Structures.stacks_and_queues.stacks_and_queues import Stack, Queue


def test_stack(stack_test):
    """
    Can successfully instantiate an empty stack
    Can successfully push onto a stack
    Can successfully push multiple values onto a stack 
    Can successfully peek the next item on the stack
    """
    stack_empty = Stack()
    expected = "NULL"
    actual = f"{stack_empty}"
    assert actual == expected
    actual = f"{stack_test}"
    expected = "2 -> 1 -> 0 -> NULL"
    assert actual == expected
    actual = stack_test.peek()
    expected = 2
    assert actual == expected


def test_stack_pop(stack_test,stack_test_pop):
    """
    Can successfully pop off the stack
    Can successfully empty a stack after multiple pops
    Calling pop or peek on empty stack raises exception
    """
    actual = stack_test_pop[0]
    expected = 2
    assert actual == expected
    actual = stack_test_pop[1]
    expected = "the stack is empty"
    assert actual == expected
    actual = stack_test.peek()
    expected = "the stack is empty"
    assert actual == expected


def test_queue(queue_test):
    """
    Can successfully instantiate an empty queue
    Can successfully enqueue into a queue
    Can successfully enqueue multiple values into a queue
    Can successfully peek into a queue, seeing the expected value
    """
    queue_empty = Queue()
    expected = "NULL"
    actual = f"{queue_empty}"
    assert actual == expected
    actual = f"{queue_test}"
    expected = "0 -> 1 -> 2 -> NULL"
    assert actual == expected
    actual = queue_test.peek()
    expected = 0
    assert actual == expected


def test_queue_dequeue(queue_test,queue_test_dequeue):
    """
    Can successfully dequeue out of a queue the expected value
    Can successfully empty a queue after multiple dequeues
    Calling dequeue or peek on empty queue raises exception
    """
    actual = queue_test_dequeue[0]
    expected = 0
    assert actual == expected
    actual = queue_test_dequeue[1]
    expected = "the queue is empty"
    assert actual == expected
    actual = queue_test.peek()
    expected = "the queue is empty"
    assert actual == expected



@pytest.fixture
def queue():
    return Queue()

@pytest.fixture
def stack():
    return Stack()

@pytest.fixture
def queue_test(queue):
    queue.enqueue(0)
    queue.enqueue(1)
    queue.enqueue(2)
    return queue

@pytest.fixture
def stack_test(stack):
    stack.push(0)
    stack.push(1)
    stack.push(2)
    return stack

@pytest.fixture
def stack_test_pop(stack_test):
    first = stack_test.pop()
    stack_test.pop()
    stack_test.pop()
    empty = stack_test.pop()
    return first , empty 

@pytest.fixture
def queue_test_dequeue(queue_test):
    first = queue_test.dequeue()
    queue_test.dequeue()
    queue_test.dequeue()
    empty = queue_test.dequeue()
    return first , empty 