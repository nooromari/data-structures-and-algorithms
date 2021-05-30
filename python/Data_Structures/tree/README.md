# Trees
<!-- Short summary or background information -->
A tree is a widely used abstract data type that simulates a hierarchical tree structure, with a root value and subtrees of children with a parent node, represented as a set of linked nodes.

A tree data structure can be defined recursively as a collection of nodes (starting at a root node), where each node is a data structure consisting of a value, together with a list of references to nodes (the "children"), with the constraints that no reference is duplicated, and none points to the root.

## Challenge
<!-- Description of the challenge -->
Create a Node class that has properties for the value stored in the node, the left child node, and the right child node.
Create a BinaryTree class
Define a method for each of the depth first traversals called preOrder, inOrder, and postOrder which returns an array of the values, ordered appropriately.
Any exceptions or errors that come from your code should be semantic, capturable errors. For example, rather than a default error thrown by your language, your code should raise/throw a custom, semantic error that describes what went wrong in calling the methods you wrote for this lab.

Create a BinarySearchTree class
Define a method named add that accepts a value, and adds a new node with that value in the correct location in the binary search tree.
Define a method named contains that accepts a value, and returns a boolean indicating whether or not the value is in the tree at least once.

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
Big O:
- time -> log(n)
- space -> O(1)

## API
<!-- Description of each method publicly available in each of your trees -->
### BinaryTree class
- method `preOrder`, `inOrder`, and `postOrder` which returns an array of the values, ordered appropriately.

### BinarySearchTree class
- `add` that accepts a value, and adds a new node with that value in the correct location in the binary search tree.
- `contains` that accepts a value, and returns a boolean indicating whether or not the value is in the tree at least once.


## Challenge 16 summary:
<!-- Description of the challenge -->
Write an instance method called `find-maximum-value`. Without utilizing any of the built-in methods available to your language, return the maximum value stored in the tree. You can assume that the values stored in the Binary Tree will be numeric.

## Whiteboard Process
<!-- Embedded whiteboard image -->
![find-maximum-binary-tree](../../challenges/assets/find-maximum-binary-tree.jpg)

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
Big O:
- time -> O(n)
- space -> O(n)

## Solution
<!-- Show how to run your code, and examples of it in action -->

```
  print(binary_tree.find_maximum_value())
```
output: max number


Note: *collaburate with tala and manar*