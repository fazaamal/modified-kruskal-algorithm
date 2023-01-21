import heapq

def modified_kruskal(nodes, edges, b):
    # Determine the minimum cost (min) and the maximum cost (max) from all the costs of edges in the graph.
    min_cost = min(edge[2] for edge in edges)
    max_cost = max(edge[2] for edge in edges)
    
    # Determine the range (max – min)
    range_cost = max_cost - min_cost
    
    # Determine the interval of each box (interval = range / b; and the result is rounded up)
    interval = (range_cost + b - 1) // b
    
    # Insert all edges into the appropriate box.
    boxes = [[] for _ in range(b)]
    for edge in edges:
        box_index = (edge[2] - min_cost) // interval
        if box_index < b:
            boxes[box_index].append(edge)
            
    # Sort all edges within the boxes into min heaps.
    for box in boxes:
        heapq.heapify(box)
    
    # initialize the disjoint set
    disjoint_set = {node: node for node in nodes}
    
    # create an empty list to store the minimum spanning tree
    mst = []
    
    for box in boxes:
        while box:
            # remove the minimum edge (the root of the heap)
            u, v, w = heapq.heappop(box)
            if find(u, disjoint_set) != find(v, disjoint_set):
                # add the edge to the minimum spanning tree
                mst.append((u, v, w))
                union(u, v, disjoint_set)
            if len(mst) == len(nodes) - 1:
                return mst
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
    
nodes = [1, 2, 3, 4]
edges = [(1, 2, 2), (1, 3, 1), (3, 2, 3), (3, 4, 5), (4, 2, 4)]
result = modified_kruskal(nodes, edges, 2)
printResult(result)