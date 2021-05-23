# Challenge Summary
<!-- Description of the challenge -->
Create a brand new PseudoQueue class. Do not use an existing Queue. Instead, this PseudoQueue class will implement our standard queue interface (the two methods listed below), but will internally only utilize 2 Stack objects. Ensure that you create your class with the following methods:

enqueue(value) which inserts value into the PseudoQueue, using a first-in, first-out approach.
dequeue() which extracts a value from the PseudoQueue, using a first-in, first-out approach.
The Stack instances have only push, pop, and peek methods. You should use your own Stack implementation. Instantiate these Stack objects in your PseudoQueue constructor.

## Whiteboard Process
<!-- Embedded whiteboard image -->

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
- enqueue :
time Big O(1)
space Big O(1)

- dequeue :
time Big O(n)
space Big O(n)

## Solution
<!-- Show how to run your code, and examples of it in action -->

- enqueue method 

*Example*

```
queue = Pseudo_Queue()
queue.enqueue(5)
queue.enqueue(9)
```

*output* `9 -> 5 -> NULL`

```
queue.dequeue()
print(queue)
```
*output* `9 -> NULL`

