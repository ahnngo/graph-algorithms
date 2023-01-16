class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
        self.visited = [False for i in range(self.V)]

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    # path compression
    def find(self, parent, ele):
        if ele != parent[ele]:
            parent[ele] = self.find(parent, parent[ele])
        return parent[ele]

    # union by rank
    def union(self, parent, rank, x, y):
        if rank[x] < rank[y]:
            parent[x] = y
        elif rank[x] > rank[y]:
            rank[y] = x
        else:
            parent[y] = x
            rank[x] += 1

    def kruskal(self):
        mst = []

        # step 1: sort all edges
        self.graph = sorted(self.graph, key=lambda item: item[2])

        parent, rank = [], []

        # create subsets
        for v in range(self.V):
            parent.append(v)
            rank.append(0)

        edges = 0
        i = 0
        while edges < self.V - 1:
            # step 2: pick the smallest edge
            u, v, w = self.graph[i]
            i += 1

            x = self.find(parent, u)
            y = self.find(parent, v)

            # include the edge if its not making cycle
            if x != y:
                mst.append([u, v, w])
                edges += 1
                self.union(parent, rank, x, y)

        min_cost = 0
        for u, v, w in mst:
            min_cost += w
            print("%d -- %d : %d" % (u, v, w))

        print("Minimum cost: ", min_cost)


# Driver code
graph = Graph(8)

graph.add_edge(2, 6, 2)
graph.add_edge(2, 7, 9)
graph.add_edge(4, 2, 1)
graph.add_edge(4, 3, 8)
graph.add_edge(0, 1, 8)
graph.add_edge(3, 7, 7)
graph.add_edge(0, 5, 4)
graph.add_edge(4, 0, 2)
graph.add_edge(2, 3, 4)
graph.add_edge(0, 3, 6)
graph.add_edge(2, 1, 10)
graph.add_edge(3, 5, 8)
graph.add_edge(6, 1, 7)

graph.kruskal()
