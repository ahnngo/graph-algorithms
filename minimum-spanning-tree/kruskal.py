class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
        self.visited = [False for i in range(self.V)]
        # self.parent maps a node to a parent it is associated with
        # self.rank maps a node to its ranking for union
        self.parent, self.rank = {}, {}
        for i in range(self.V):
            self.parent[i] = i
            self.rank[i] = 0

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def find(self, v):
        while v != self.parent[v]:
            # path compression
            # if the vertex is not the same as the parent, move to the vertex upper the tree
            self.parent[v] = self.parent[self.parent[v]]
            v = self.parent[v]
        # return the parent
        return v

    # union by rank
    def union(self, x, y):
        if self.rank[x] < self.rank[y]:
            self.parent[x] = y
        elif self.rank[x] > self.rank[y]:
            self.rank[y] = x
        else:
            self.parent[y] = x
            self.rank[x] += 1

    def kruskal(self):
        mst = []

        # step 1: sort all edges
        self.graph = sorted(self.graph, key=lambda item: item[2])
        print(self.graph)

        edges = 0
        i = 0
        while edges < self.V - 1:
            # step 2: pick the smallest edge
            u, v, w = self.graph[i]
            i += 1

            x = self.find(u)
            y = self.find(v)

            # include the edge if its not making cycle
            if x != y:
                mst.append([u, v, w])
                edges += 1
                self.union(x, y)

        min_cost = 0
        for u, v, w in mst:
            min_cost += w
            print("%d -- %d : %d" % (u, v, w))

        print("Minimum cost: ", min_cost)


# Driver code
g = Graph(4)
g.add_edge(0, 1, 10)
g.add_edge(0, 2, 6)
g.add_edge(0, 3, 5)
g.add_edge(1, 3, 15)
g.add_edge(2, 3, 4)

g.kruskal()
