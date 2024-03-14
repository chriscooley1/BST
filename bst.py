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

    def _in_order_traversal_recursive(self, node, result):
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
        return self._height_recursive(self.root)

    def _height_recursive(self, node):
        if not node:
            return -1
        return 1 + max(self._height_recursive(node.left), self._height_recursive(node.right))

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
        return ','.join(map(str, serialized_tree))

    def _serialize_recursive(self, node, serialized_tree):
        if node:
            serialized_tree.append(node.value)
            self._serialize_recursive(node.left, serialized_tree)
            self._serialize_recursive(node.right, serialized_tree)
        else:
            serialized_tree.append(None)

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