import unittest
from bst import BST 

class TestBSTMethods(unittest.TestCase):
    def setUp(self):
        self.bst = BST()
        self.bst.insert(5)
        self.bst.insert(3)
        self.bst.insert(7)
        self.bst.insert(2)
        self.bst.insert(4)
        self.bst.insert(6)
        self.bst.insert(8)

    def test_insert(self):
        self.assertEqual(self.bst.root.value, 5)
        self.assertEqual(self.bst.root.left.value, 3)
        self.assertEqual(self.bst.root.right.value, 7)
        self.assertEqual(self.bst.root.left.left.value, 2)
        self.assertEqual(self.bst.root.left.right.value, 4)
        self.assertEqual(self.bst.root.right.left.value, 6)
        self.assertEqual(self.bst.root.right.right.value, 8)

    def test_search(self):
        self.assertTrue(self.bst.search(5))
        self.assertTrue(self.bst.search(3))
        self.assertTrue(self.bst.search(7))
        self.assertTrue(self.bst.search(2))
        self.assertTrue(self.bst.search(4))
        self.assertTrue(self.bst.search(6))
        self.assertTrue(self.bst.search(8))
        self.assertFalse(self.bst.search(1))
        self.assertFalse(self.bst.search(9))

    def test_in_order_traversal(self):
        self.assertEqual(self.bst.in_order_traversal(), [2, 3, 4, 5, 6, 7, 8])

    def test_find_min(self):
        self.assertEqual(self.bst.find_min(), 2)

    def test_find_max(self):
        self.assertEqual(self.bst.find_max(), 8)

    def test_height(self):
        self.assertEqual(self.bst.height(), 2)

    def test_count_leaves(self):
        self.assertEqual(self.bst.count_leaves(), 4)

    def test_serialize_deserialize(self):
        serialized_tree = self.bst.serialize()
        new_bst = BST()
        new_bst.deserialize(serialized_tree)
        self.assertEqual(self.bst.in_order_traversal(), new_bst.in_order_traversal())

if __name__ == '__main__':
    unittest.main()
