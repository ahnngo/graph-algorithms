import heapq


def prim(graph, start):
    """
    :param graph: adjacency matrix of graph
    :param start: starting vertex to create the minimum spanning tree
    :return: minimum spanning tree and the total cost
    """
    mst = [start]
    totalCost = 0
    visited = [False] * len(graph)
    visited[start] = True
    edges = []
    # push edges from the starting vertex to the heap
    for node in range(len(graph)):
        if graph[start][node] != 0:
            edges.append([graph[start][node], start, node])
    heapq.heapify(edges)

    while edges:
        cost, frm, to = heapq.heappop(edges)
        if not visited[to]:
            visited[to] = True
            mst.append(to)
            totalCost += cost
            print(frm, '-', to, ':', cost)
            for to_next in range(len(graph)):
                if graph[to][to_next] != 0 and not visited[to_next]:
                    heapq.heappush(edges, [graph[to][to_next], to, to_next])

    if len(mst) != len(graph):
        return None, None

    return mst, totalCost


myGraph = [[0, 3, 0, 0, 8],
         [3, 0, 4, 2, 0],
         [0, 4, 0, 10, 0],
         [0, 2, 10, 11, 0],
         [8, 0, 0, 11, 0]]

mst, cost = prim(myGraph, 0)

print("Minimum Spanning Tree:", mst)
print("Total cost:", cost)

