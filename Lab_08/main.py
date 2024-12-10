'''
Dylan Davis
3047302
EECS 330
11/6/23
Binary tree traversal: Preorder Traversal, Inorder Traversal, and Postorder Traversal
'''

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def preorder_traversal(self) -> list:
        """Implement preorder traversal."""
        r = []
        stack = [self.root] if self.root is not None else [] # creates a stack that when not empty has root node
        while stack: # while in the stack 
            n = stack.pop() # pop the last node (n) from the stack 
            r.append(n.value) # add the popped value to the list of results (r)
            if n.right: # if the right child exists, process the right first 
                stack.append(n.right) # move the right child to the stack 
            if n.left: # if the left child exists 
                stack.append(n.left) # add the left child to the stack 
        return r # return the updates list of results   
    pass

    def inorder_traversal(self) -> list:
        """Implement inorder traversal."""
        r = [] # empty list to hold the results (r) returned at the end 
        stack = [] # our friend the stack returns
        now = self.root # start from the root
        while stack or now: # while at starting point at root
            if now: # if at root index 
                stack.append(now) # add root node
                now = now.left # slide child to the left 
            else:
                now = stack.pop() # pop the top of the stack 
                r.append(now.value) # and add the root value of the node to the stack 
                now = now.right # slide the child to the right
        return r 
    pass

    def postorder_traversal(self) -> list:
        """Implement postorder traversal."""
        r = []
        stack =[self.root] if self.root is not None else [] # create stack once again with root node 
        while stack: # while in stack 
            n = stack.pop() # pop the last value from stack 
            r.insert(0, n.value) # add value of node (n) to the 0 index of the list of results (r)
            if n.left: # if the left child exists 
                stack.append(n.left) # slide to the left 
            if n.right: # if the right child exists 
                stack.append(n.right) #slide to the left 
        return r # return the list of out comes 
    pass

'''Implementation of Graph Traversal'''
class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjacency_list = [[] for _ in range(vertices)]

    def add_edge(self, u, v):
        """Add an edge between vertices u and v."""
        self.adjacency_list[u].append(v) # add v value to adjacent list of u's
    pass

    def dfs(self, source):
        """Implement Depth-First Search (DFS) starting from the source vertex."""
        p = [False] * self.vertices # previous(p) finds pervious vertices
        r = [] # empty list to track traveral 
        stack = [source] # stack with vertex at source
        while stack:
            vertex = stack.pop() 
            if not p[vertex]: 
                p[vertex] = True # mark vertexes that have been traversed
                r.append(vertex) # append to the list of traversed
                stack.extend(neighbor for neighbor in self.adjacency_list[vertex] if not p[neighbor]) #lengthen stack 
        return r # return traversed
    pass

    def bfs(self, source):
        """Implement Breadth-First Search (BFS) starting from the source vertex."""
        p = [False] * self.vertices # pervious(p) track vertixes weve been too
        r = [] # store traversed 
        queue = [source] # queue with source vertex

        while queue: 
            vertex = queue.pop(0) # vertext = the poped front of the queue 
            if not p[vertex]: # if not traversed
                p[vertex] = True # mark 
                r.append(vertex) # add to the list of traversed
                queue.extend(neighbor for neighbor in self.adjacency_list[vertex] if not p[neighbor]) # extened the queue 
        return r
    pass

'''Test'''
# Create a binary tree
bt = BinaryTree()
bt.root = TreeNode(1)
bt.root.left = TreeNode(2)
bt.root.right = TreeNode(3)
bt.root.left.left = TreeNode(4)
bt.root.left.right = TreeNode(5)
bt.root.right.left = TreeNode(6)
bt.root.right.right = TreeNode(7)
bt.root.left.left.left = TreeNode(8)
bt.root.left.left.right = TreeNode(9)
bt.root.right.right.right = TreeNode(10)

# Test the traversals
print("Preorder Traversal:", bt.preorder_traversal())
print("Inorder Traversal:", bt.inorder_traversal())    
print("Postorder Traversal:", bt.postorder_traversal())

# -------------------------------------------

# Create a graph with 20 vertices
graph = Graph(20)

# Add edges (change as needed)
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 3)
graph.add_edge(1, 4)
graph.add_edge(2, 5)
graph.add_edge(2, 6)
graph.add_edge(3, 7)
graph.add_edge(3, 8)
graph.add_edge(4, 9)
graph.add_edge(4, 10)
graph.add_edge(5, 11)
graph.add_edge(5, 12)
graph.add_edge(6, 13)
graph.add_edge(6, 14)
graph.add_edge(7, 15)
graph.add_edge(7, 16)
graph.add_edge(8, 17)
graph.add_edge(8, 18)
graph.add_edge(9, 19)

# Test DFS and BFS from a source vertex
print("DFS from vertex 0:", graph.dfs(0))  
print("BFS from vertex 0:", graph.bfs(0))

# Create a graph with 4 vertices
graph = Graph(4)
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)
graph.add_edge(2, 0)
graph.add_edge(2, 3)
graph.add_edge(3, 3)

# Test DFS and BFS from a source vertex
print("DFS from vertex 2:", graph.dfs(2))
print("BFS from vertex 2:", graph.bfs(2))