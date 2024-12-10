# Part C
class TreeNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None


class TreeMap:
    def __init__(self):
        self.root = None

    def put(self, key, value):  # function to insert key value pairs
        self.root = self._put_recursive(self.root, key, value)

    def _put_recursive(self, node, key, value): # function to insert a node into the tree

        if node is None:
            return TreeNode(key, value)

        if key < node.key:
            node.left = self._put_recursive(node.left, key, value)
        elif key > node.key:
            node.right = self._put_recursive(node.right, key, value)
        else:
            node.value = value

        return node

    def get(self, key): # function to retrieve key value pairs
        return self._get_recursive(self.root, key)

    def _get_recursive(self, node, key): # fuction to get keys using recursion
        if node is None:
            return None
        if key == node.key:
            return node.value
        elif key < node.key:
            return self._get_recursive(node.left, key)
        else:
            return self._get_recursive(node.right, key)
