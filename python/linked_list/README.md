# Singly Linked List

A Linked List is a sequence of Nodes that are connected/linked to each other. The most defining feature of a Linked List is that each Node references the next Node in the link.

## Challenge

Create a Node class that has properties for the value stored in the Node, and a pointer to the next Node.
Within the LinkedList class, include a head property. Upon instantiation, an empty Linked List should be created.

## Approach & Efficiency

### Approach
Singly Linked List

### Efficiency
 - **Big O :**
   - O(1) Time/space performance for **insert** method.
   - O(n) Time and O(1) space performance for **includes** method.


## API

- **insert**: 
a method takes any value as an argument and adds a new node with that value to the head of the list with.

- **includes** : 
a method takes any value as an argument and returns a boolean result depending on whether that value exists as a Node’s value somewhere within the list.


- [code](linked_list.py)

