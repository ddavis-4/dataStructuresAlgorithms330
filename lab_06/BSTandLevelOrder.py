# Part A the implementation of a BST
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, key):
        self.size += 1  # increase size by 1 to make space to insert
        if self.root is None:  # if the tree is empty
            self.root = TreeNode(key)  # create a tree node with key
        else:
            self._rec_insert(key, self.root)

    def _rec_insert(self, key, local_root):
        if key >= local_root.value:
            if local_root.right is None:
                local_root.right = TreeNode(key)
            else:
                self._rec_insert(key, local_root.right)
        else:
            if local_root.left is None:
                local_root.left = TreeNode(key)
            else:
                self._rec_insert(key, local_root.left)

    def get_size(self):  # returns the size
        return self.size

    def contains_key(self, key):  # check to see if keys are contained with in tree
        if self.root is None:
            return False
        return self.search(key) is not None

    def search(self, key) -> TreeNode:  # function that check for keys starting at the root
        return self._rec_search(key, self.root)

    def _rec_search(self, key, cur_node):
        if cur_node is None:
            return None
        if key == cur_node.value:
            return cur_node
        if key < cur_node.value:
            return self._rec_search(key, cur_node.left)
        if key > cur_node.value:
            return self._rec_search(key, cur_node.right)
        else:
            raise RuntimeError("Key not found")

    # Part B: level order traversal

    def level_order_traversal(self) -> list:  # level order traversal function
        result = []  # empty list
        queue = [self.root]  # list queue starting at root node

        while queue:
            node = queue.pop(0)  # pop front
            if node:
                result.append(node.value)  # append current to list of values
                if node.left:
                    queue.append(node.left)  # if left child exists enqueue
                if node.right:
                    queue.append(node.right)  # if right child exists enqueue
        return result
