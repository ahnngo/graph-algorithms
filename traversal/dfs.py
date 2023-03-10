class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for i in range(self.V)]  # adjacency list presentation
        self.visited = [False for i in range(self.V)]

    def add_edge(self, src, dest):
        self.graph[src].append(dest)

    def dfs_traversal(self, v):
        self.visited[v] = True
        print(v, end=' ')

        # recur for all adjacent vertices
        for adj in self.graph[v]:
            if not self.visited[adj]:
                self.dfs_traversal(adj)


graph = Graph(13)

graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(1, 5)
graph.add_edge(2, 4)
graph.add_edge(2, 10)
graph.add_edge(2, 5)
graph.add_edge(2, 7)
graph.add_edge(3, 6)
graph.add_edge(4, 7)
graph.add_edge(5, 2)
graph.add_edge(5, 8)
graph.add_edge(6, 9)
graph.add_edge(8, 11)
graph.add_edge(11, 12)

print("DFS Recursive")
graph.dfs_traversal(1)

