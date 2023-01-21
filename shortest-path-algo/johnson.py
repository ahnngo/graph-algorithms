class Graph:

    def __init__(self, graph):
        self.v = len(graph)
        self.graph = graph
        self.visited = [False for i in range(self.v)]
        self.dist = [float("inf")] * self.v
        self.edges = []
        self.new_graph = [[0 for x in range(self.v)] for y in range(self.v)]

    def add_edge(self):
        for u in range(self.v):
            for v in range(self.v):
                if self.graph[u][v] != 0:
                    self.edges.append([u, v, self.graph[u][v]])

    def bellman_ford(self):
        # create an arbitrary source node. The distance to that node is 0
        self.dist.append(0)

        # add edges to all the other vertices from arbitrary source
        arbitrary_edges = 0
        for i in range(self.v):
            self.edges.append([self.v, i, 0])
            arbitrary_edges += 1

        # relax v time (v - 1 if count the arbitrary source)
        for i in range(self.v):
            for (u, v, w) in self.edges:
                # If there is a path from the source to u existing and
                # the cost from u to v is less than what already exists from source to v
                # Update the cost and update the path
                if self.dist[u] != float('inf') and self.dist[u] + w < self.dist[v]:
                    self.dist[v] = self.dist[u] + w

        # discard the arbitrary source
        self.dist.pop()
        for i in range(arbitrary_edges):
            self.edges.pop()

    def find_min_vertex(self):
        min_vertex = -1
        for i in range(self.v):
            if (min_vertex == -1 or self.dist[min_vertex] > self.dist[i]) and not self.visited[i]:
                min_vertex = i
        return min_vertex

    def dijkstra(self, src):
        # reset visited tracking list and distance
        self.visited = [False for i in range(self.v)]
        self.dist = [float("inf")] * self.v
        self.dist[src] = 0

        for i in range(self.v - 1):
            min_vertex = self.find_min_vertex()
            self.visited[min_vertex] = True
            for j in range(self.v):
                if self.graph[min_vertex][j] != 0 and not self.visited[j]:
                    new_dist = self.dist[min_vertex] + self.new_graph[min_vertex][j]
                    if new_dist < self.dist[j]:
                        self.dist[j] = new_dist
        for i in range(self.v):
            print(i, " ", self.dist[i])

    def johnson(self):
        self.add_edge()
        self.bellman_ford()

        # create new graph with positive edges weights
        for u in range(self.v):
            for v in range(self.v):
                if self.graph[u][v] != 0:
                    self.new_graph[u][v] = self.dist[u] + self.graph[u][v] - self.dist[v]

        print("New Graph: ", str(self.new_graph))

        # run Dijkstra for every vertex as source
        for src in range(self.v):
            print("Shortest Distance from vertex: ", src)
            self.dijkstra(src)


graph = [[0, 4, 0, 0, 1],
         [0, 0, 0, 0, 0],
         [0, 7, 0, -2, 0],
         [0, 1, 0, 0, 0],
         [0, 0, 0, -5, 0]]

# Johnson's algo
g = Graph(graph)
g.johnson()
