'''
Dylan Davis
3047302
EECS 330
11/13/2023
implementing advanced graph algorithms 
'''
import sys #import

#A: Implement Dijkstra's Shortest Path Tree Algorithm
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def add_edge(self, u, v, w):
        self.graph[u][v] = w
        self.graph[v][u] = w

    def dijkstra(self, src):
        # Stores shortest distance.
        dist = [sys.maxsize] * self.V
        # Shortest distance to the same node is 0.
        dist[src] = 0

        # Your code.
        marked = [False] * self.V # an array to keep track of nodes we have visited

        for i in range(self.V - 1): #loop to go through array
            minDistance = sys.maxsize # find the closest vertex that hasn't been touched
            minDistanceIndex = -1

            for vertex in range(self.V): #go through all the vertexes
                if not marked[vertex] and dist[vertex] < minDistance: #if the vertex has not been makred and is less than min distance 
                    minDistance = dist[vertex]
                    minDistanceIndex = vertex #set the closest distance to vertex
            marked[minDistanceIndex] = True #mark the current vertex

            for neighbor, weight in enumerate(self.graph[minDistanceIndex]): #check to see if the neighbor was visited and check edge weight
                if not marked[neighbor] and weight > 0: # if statement to find the new distance for a new neighbor
                    newDistance = dist[minDistanceIndex] + weight
                    if newDistance < dist[neighbor]:
                        dist[neighbor] = newDistance

        # You have to call print_solution by passing dist.
        # In this way everyone's output would be standardized.
        self.print_dijkstra(dist)

    def print_dijkstra(self, dist):
        print("Vertex \t Distance from Source")
        for node in range(self.V):
            print(f"{node} \t->\t {dist[node]}")

#B: Implement Prim's Minimum Spanning Tree
    def prim(self):
        # Store the resulting graph.
        # where result[i] keeps the source vertex.
        # See the example output for expected result.
        result = [None] * self.V

        # Your code
        k = [float('inf')] * self.V #array(k) to store key values for all of the vertices
        k[0] = 0  #set key value first vertex = 0 to make it the source of MST
        p_q = list(range(self.V)) #a priority queue to store vertices with key values

        while p_q: #will loop until pq is empty 
            minWeightIndex = min(p_q, key=lambda x: k[x]) #find vertex with lowest key value in p-queue
            markedVertex = p_q.pop(p_q.index(minWeightIndex))

            for v, weight in enumerate(self.graph[markedVertex]): #go through nearby vertices of of marked vertexs
                if weight > 0 and v in p_q and weight < k[v]: #check if there is an edge and if neighboring vertex is still in the queue
                    k[v] = weight
                    result[v] = markedVertex

        # You have to call print_solution by passing the output graph.
        # In this way everyone's output would be standardized.
        self.print_prim(result)

    def print_prim(self, result):
        print("Edge \t Weight")
        for i in range(1, self.V):
            print(f"{result[i]} - {i} \t {self.graph[i][result[i]]}")


#C: Kruskal's Minimum Spanning Tree
    def kruskal_mst(self):
        # Your code.
        result = [] #empty list of results
        totEdges = []
        for i in range(self.V): #for loop to iterate through pairs of vertices and their weights forming the edges
            for j in range(i + 1, self.V): #checks for the edges
                if self.graph[i][j] > 0:
                    totEdges.append((i, j, self.graph[i][j]))
        totEdges.sort(key=lambda x: x[2]) # organize edges based on their weights
        parentNode = [i for i in range(self.V)] #make array for vertex parents
        rankNodes = [0] * self.V #arrary for rank of nodes

        def findParentRoot(node): #function created to find the roots parent
            if parentNode[node] == node: #if the parent node is current, declare it the parent
                return node
            return findParentRoot(parentNode[node])

        def unionofSets(node_i, node_j): #function created for the union of sets 
            r_i = findParentRoot(node_i)
            r_j = findParentRoot(node_j)
            #union based on the rank of nodes
            if rankNodes[r_i] < rankNodes[r_j]:
                parentNode[r_i] = r_j
            elif rankNodes[r_i] > rankNodes[r_j]:
                parentNode[r_j] = r_i
            else:
                parentNode[r_i] = r_j 
                rankNodes[r_j] += 1

        for edge in totEdges: #loop to go through sorted edges and add to result arrary from before
            u, v, weight = edge
            r_u = findParentRoot(u)
            r_v = findParentRoot(v)
            #check if adding an edge forms a circle in MST
            if r_u != r_v: 
                result.append((u, v, weight))
                unionofSets(r_u, r_v) 

        # Similar to the previous e.g. print your
        # resulting graph.
        self.print_kruskal(result)

    def print_kruskal(self, result):
        print("Edge \t Weight")
        # Note that the below code is slightly different than the Prim's.
        # You can change this print code according to your choice, but
        # you have to display your graph in (vertex->vertex weight) format.
        for edge in result:
            print(f"{edge[0]} -> {edge[1]} \t {edge[2]}")


# D. Testing
# Create a graph with 21 vertices.
graph = Graph(21)

# Add edges and their weights.
graph.add_edge(0, 1, 4)
graph.add_edge(0, 2, 1)
graph.add_edge(1, 3, 3)
graph.add_edge(2, 4, 2)
graph.add_edge(3, 5, 2)
graph.add_edge(4, 6, 2)
graph.add_edge(5, 7, 2)
graph.add_edge(7, 8, 2)
graph.add_edge(6, 8, 2)

graph.add_edge(8, 9, 5)
graph.add_edge(8, 10, 4)
graph.add_edge(9, 11, 3)
graph.add_edge(10, 11, 1)

graph.add_edge(11, 12, 1)
graph.add_edge(12, 13, 1)
graph.add_edge(13, 14, 1)

graph.add_edge(14, 15, 1)
graph.add_edge(14, 16, 10)
graph.add_edge(15, 17, 1)
graph.add_edge(16, 20, 1)
graph.add_edge(17, 18, 1)
graph.add_edge(18, 19, 1)
graph.add_edge(19, 20, 1)

# Run Dijkstra's algorithm from source vertex 0.
graph.dijkstra(0)

# Find and print the Prim's Minimum Spanning Tree (MST).
graph.prim()

# Find and print the Kruskal's Minimum Spanning Tree (MST).
graph.kruskal_mst()
