# Binary Search Tree

## YOU MUST USE THONNY

Unless you decide you are beyond what benefit Thonny can provide, then you may use the terminal. But you should use Thonny. But under no circumstances should you use vscode or anything similar. Especially not chatgpt and not copilot (double especially not copilot, it won't be helpful at this stage).

Implement a BST. It should include these methods:

- insert(self, int) -> None - inserts a number into the tree
- search(self, int) -> bool - returns whether or not a value is in the tree
- in_order_traversal(self) -> list[int] - returns a list of all the values in sorted order
- find_min(self) -> int - returns the smallest number in the tree (you cannot turn the tree into a list then return an element from the list, you must do it by traversing the tree)
- find_max(self) -> int - returns the largest number in the tree (you cannot turn the tree into a list then return an element from the list, you must do it by traversing the tree)
- height(self) -> int - returns the depth of the tree (how far is the furthest node from the root node?)
- count_leaves(self) -> int - returns the number of leaf nodes in the tree (leaf nodes are nodes without any children)
- serialize(self) -> str - turn the BST into a string
- deserialize(self, tree: str) -> None - deserialize a serialized BST (take a string version of a BST and make an empty BST filled with those values). The new tree should match the tree that was serialized.

Add unit tests for each of these methods.

Submit a link to your github repo with your code.

## Extra Challenge

Implement the delete method. 

## Extra Extra Challenge

Implement tree balancing.