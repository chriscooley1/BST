class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = TreeNode(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if not node.left:
                node.left = TreeNode(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if not node.right:
                node.right = TreeNode(value)
            else:
                self._insert_recursive(node.right, value)

    def search(self, value):
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        if not node:
            return False
        if node.value == value:
            return True
        elif value < node.value:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)

    def in_order_traversal(self):
        result = []
        self._in_order_traversal_recursive(self.root, result)
        return result

    def _in_order_traversal_recursive(self, node, result=None):
        if result is None:
            result = []
        if node:
            self._in_order_traversal_recursive(node.left, result)
            result.append(node.value)
            self._in_order_traversal_recursive(node.right, result)

    def find_min(self):
        if not self.root:
            return None
        node = self.root
        while node.left:
            node = node.left
        return node.value

    def find_max(self):
        if not self.root:
            return None
        node = self.root
        while node.right:
            node = node.right
        return node.value

    def height(self):
        return self._height_recursive(self.root) - 1 if self.root else 0

    def _height_recursive(self, node):
        if not node:
            return 0
        left_height = self._height_recursive(node.left)
        right_height = self._height_recursive(node.right)
        return 1 + max(left_height, right_height)

    def count_leaves(self):
        return self._count_leaves_recursive(self.root)

    def _count_leaves_recursive(self, node):
        if not node:
            return 0
        if not node.left and not node.right:
            return 1
        return self._count_leaves_recursive(node.left) + self._count_leaves_recursive(node.right)

    def serialize(self):
        serialized_tree = []
        self._serialize_recursive(self.root, serialized_tree)
        return ','.join(serialized_tree)

    def _serialize_recursive(self, node, serialized_tree):
        if not node:
            serialized_tree.append('None')
        else:
            serialized_tree.append(str(node.value))
            self._serialize_recursive(node.left, serialized_tree)
            self._serialize_recursive(node.right, serialized_tree)

    def deserialize(self, tree):
        values = tree.split(',')
        self.root = self._deserialize_recursive(values)

    def _deserialize_recursive(self, values):
        if not values:
            return None
        value = values.pop(0)
        if value == 'None':
            return None
        node = TreeNode(int(value))
        node.left = self._deserialize_recursive(values)
        node.right = self._deserialize_recursive(values)
        return node
    
    def delete(self, value):
        self.root = self._delete_recursive(self.root, value)

    def _delete_recursive(self, node, value):
        if not node:
            return node

        if value < node.value:
            node.left = self._delete_recursive(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursive(node.right, value)
        else:  # Found the node to delete
            # Case 1: Node to delete is a leaf node or has only one child
            if not node.left:
                return node.right
            elif not node.right:
                return node.left

            # Case 2: Node to delete has two children
            min_node = self._find_min_node(node.right)
            node.value = min_node.value
            node.right = self._delete_recursive(node.right, min_node.value)

        return node

    def _find_min_node(self, node):
        while node.left:
            node = node.left
        return node