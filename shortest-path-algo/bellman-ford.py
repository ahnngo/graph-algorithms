class Graph:

    def __init__(self, v):
        self.v = v
        self.graph = []
        self.dist = [float("inf")] * self.v
        self.path = [[i] for i in range(self.v)]

    def add_edge(self, s, d, w):
        self.graph.append([s, d, w])

    def bellman_ford(self, src):
        """
        Time complexity: O(VE)
        """
        self.dist[src] = 0

        # relax v-1
        for i in range(self.v - 1):
            # u for source, v for dest, and c for cost
            for u, v, c in self.graph:
                # If there is a path from the source to u existing and
                # the cost from u to v is less than what already exists from source to v
                # Update the cost and update the path
                if self.dist[u] != float('inf') and self.dist[u] + c < self.dist[v]:
                    self.dist[v] = self.dist[u] + c
                    self.path[v] = self.path[u] + [v]

        # detect negative cycles
        for u, v, c in self.graph:
            if self.dist[u] != float('inf') and self.dist[u] + c < self.dist[v]:
                print("Graph contains negative cycle")

        print("Vertex distance from source: ")
        for i in range(self.v):
            print(i, " : ", self.dist[i], "\tPath: ", self.path[i])


g = Graph(6)
g.add_edge(0, 1, 8)
g.add_edge(0, 5, 5)
g.add_edge(0, 3, 3)
g.add_edge(1, 2, 6)
g.add_edge(2, 4, 4)
g.add_edge(3, 4, -1)
g.add_edge(5, 1, -4)
g.add_edge(5, 2, -1)
g.add_edge(5, 4, -3)
g.bellman_ford(0)


