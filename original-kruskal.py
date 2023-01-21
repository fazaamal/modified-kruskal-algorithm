import heapq

def kruskal(nodes, edges):
    # initialize the disjoint set
    disjoint_set = {node: node for node in nodes}
    
    # sort the edges by weight
    edges = sorted(edges, key=lambda x: x[2])
    
    # create an empty list to store the minimum spanning tree
    mst = []
    
    # iterate through the edges
    for edge in edges:
        u, v, w = edge
        if find(u, disjoint_set) != find(v, disjoint_set):
            # add the edge to the minimum spanning tree
            mst.append(edge)
            union(u, v, disjoint_set)
    
    return mst

def find(node, disjoint_set):
    # find the root of the set
    if disjoint_set[node] != node:
        disjoint_set[node] = find(disjoint_set[node], disjoint_set)
    return disjoint_set[node]

def union(u, v, disjoint_set):
    # merge two sets
    disjoint_set[find(u, disjoint_set)] = find(v, disjoint_set)

def printResult(result):
    total = 0
    for arr in result:
        print(f'{arr[0]} - {arr[1]}: {arr[2]}')
        total += arr[2]
    
    print('Minimum total weight = ', str(total))
    
nodes = [1, 2, 3, 4, 5, 6]
edges = [(1, 2, 2), (1, 3, 1), (3, 2, 3), (3, 4, 5), (4, 2, 4), (1,6, 10), (2,6,1), (4,5,1), (3,5, 2)]
result = kruskal(nodes, edges)
printResult(result)