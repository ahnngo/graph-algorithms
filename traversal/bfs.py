from collections import deque


class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for i in range(self.V)]  # adjacency list presentation
        self.visited = [False for i in range(self.V)]

    def add_edge(self, src, dest):
        self.graph[src].append(dest)

    def bfs_traversal(self, v):
        self.visited[v] = True
        print(v, end=' ')
        queue = deque([v])
        while queue:
            node = queue.popleft()
            for adj in self.graph[node]:
                if not self.visited[adj]:
                    self.visited[adj] = True
                    queue.append(adj)
                    print(adj, end=' ')


graph = Graph(12)

graph.add_edge(1, 2)
graph.add_edge(2, 6)
graph.add_edge(6, 8)
graph.add_edge(1, 3)
graph.add_edge(8, 10)
graph.add_edge(1, 4)
graph.add_edge(3, 7)
graph.add_edge(2, 5)
graph.add_edge(6, 9)
graph.add_edge(3, 6)
graph.add_edge(8, 11)
graph.add_edge(5, 8)
graph.add_edge(7, 9)

graph.bfs_traversal(1)
