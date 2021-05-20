# Stacks and Queues
<!-- Short summary or background information -->
Stacks and Queues are data structures that consists of Nodes, but they following different concepts. 

*Stacks follow these concepts:*
- FILO : First In Last Out
- LIFO : Last In First Out

*Queues follow these concepts:*
- FIFO : First In First Out
- LILO : Last In Last Out

## Challenge
<!-- Description of the challenge -->
1. Create a `Stack` class that has a top property and contains (push, pop, peek, is_empty) methods.

2. Create a `Queue` class that has a front property and contains (enqueue, dequeue, peek, is_empty) methods.


## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
- The complicity it always Big O(1) for the time and the space .

## API
<!-- Description of each method publicly available to your Stack and Queue-->

- **Stack methods:**

| method      | Description |
| ----------- | ----------- |
| Push | takes any value as an argument and adds a new node with that value to the top of the stack |
| Pop | removes the node from the top of the stack, and returns the node’s value. |
| Peek | return the value of the top Node in the stack. |
| IsEmpty | returns true when stack is empty otherwise returns false. |


- **Queue methods:**

| method      | Description |
| ----------- | ----------- |
| Enqueue | takes any value as an argument and adds a new node with that value to the rear. |
| Dequeue | removes the node from the front of the queue, and returns the node’s value. |
| Peek | return the value of the top Node in the queue. |
| IsEmpty | returns true when queue is empty otherwise returns false. |
