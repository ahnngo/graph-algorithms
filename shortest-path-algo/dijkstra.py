class Graph:
    """
    This class will take an adjacency matrix as input, with starting_vertex that we want to start from
    """
    def __init__(self, matrix, starting_vertex=0):
        self.matrix = matrix
        self.v = len(matrix)
        self.visited = [False for i in range(self.v)]
        self.distance = [0 for i in range(self.v)]
        self.path = {}
        self.start = starting_vertex
        # Assign the distance from the starting vertex to all other nodes to infinity, except for itself.
        for i in range(self.v):
            self.path[i] = [i]
            if i == self.start:
                continue
            self.distance[i] = float('inf')



    def find_min_vertex(self):
        """
        Find the vertex that is the closest to the current visiting node that has not been yet visited
        :return: the closet node
        """
        min_vertex = -1
        for i in range(self.v):
            if (min_vertex == -1 or self.distance[min_vertex] > self.distance[i]) and not self.visited[i]:
                min_vertex = i
        return min_vertex

    def dijkstra(self):

        for i in range(self.v):
            # traverse to the closet node from the current vertex
            min_vertex = self.find_min_vertex()
            self.visited[min_vertex] = True

            for j in range(self.v):
                # from the current node, loop to all the next nodes that have not yet been visited
                # calculate the new distance to get to that node from the current node
                if self.matrix[min_vertex][j] != 0 and not self.visited[j]:
                    new_dist = self.distance[min_vertex] + self.matrix[min_vertex][j]
                    # if the new distance is less that what is currently in distance array
                    # replace the path and assign new distance to the array
                    if new_dist < self.distance[j]:
                        self.distance[j] = new_dist
                        self.path[j] = self.path[min_vertex] + [j]

        for i in range(self.v):
            print("From", self.start, "to", i, "costs" , self.distance[i], "- Path:", self.path[i])

        return self.distance






def dijkstra(adjacency_matrix):

    v = len(adjacency_matrix)
    visited = [False for i in range(v)]
    distance = [0 for i in range(v)]

    for i in range(1, v):
        distance[i] = float('inf')

    for i in range(v-1):
        min_vertex = find_min_vertex(distance, visited)
        visited[min_vertex] = True

        for j in range(v):
            if adjacency_matrix[min_vertex][j] != 0 and not visited[j]:
                new_dist = distance[min_vertex] + adjacency_matrix[min_vertex][j]
                if new_dist < distance[j]:
                    distance[j] = new_dist

    for i in range(v):
        print(i, " ", distance[i])
    pass


def find_min_vertex(distance, visited):

    min_vertex = -1
    for i in range(len(distance)):
        if (min_vertex == -1 or distance[min_vertex] > distance[i]) and not visited[i]:
            min_vertex = i
    return min_vertex


adjacency_matrix = [
    [0, 3, 5, 6, 0, 8, 0],
    [3, 0, 0, 4, 2, 0, 5],
    [5, 0, 0, 0, 0, 4, 0],
    [6, 4, 0, 0, 0, 1, 6],
    [0, 2, 0, 0, 0, 0, 10],
    [8, 0, 6, 1, 0, 0, 8],
    [0, 8, 0, 6, 10, 8, 0]
]

dijkstra(adjacency_matrix)

g = Graph(adjacency_matrix, 6)
g.dijkstra()