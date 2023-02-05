# Modified Kruskal Algorithm using a Box Sort Algorithm

This is the modified kruskal algorithm, which uses a box sort algorithm of multiple min-heaps, to increase the run time efficiency. It is based off the algorithm the paper ['MODIFIED KRUSKAL ALGORITHM USING BOX SORT FOR MINIMUM SPANNING TREE' by Bilqis Amaliah, Rarasmaya Indraswari, Ria Yunita Sari](https://www.researchgate.net/publication/332978142_MODIFIED_KRUSKAL_ALGORITHM_USING_BOX_SORT_FOR_MINIMUM_SPANNING_TREE).

## [MY REPORT ON THE TOPIC](https://docs.google.com/document/d/1-fyKkIP3FAFqF5hXuh3kRGCk7qYbzYoHf5Ny9LvVkiA/edit?usp=sharing)

## How to run the codes:
To run the original algorithm, simply run 'python original-kruskal.py' in the terminal.
To run the modified algorithm, simply run 'python modified-kruskal.py' in the terminal.

## Original Kruskal algorithm
The original algorithm simply goes as follows:
1. Sort all the edges of the graph in a single data structure, starting from the smallest edge to the largest one. 
2. Select the smallest edge that has the minimum weight and does not form a cycle in the tree, and add that edge back to the tree in its original place. If it does form a cycle, discard the edge.
3. Repeat step 2 until a spanning tree is formed.

## Modified Kruskal algorithm
The steps of the modified Kruskal algorithm:
1. Determine the minimum cost (min) and the maximum cost (max) from all the costs of edges in the graph.
2. Determine the range (max – min)
3. Determine the number of boxes (b), this may be an arbitrary number.
4. Determine the interval of each box (interval = range / b; and the result is rounded up).
5. Insert all edges into the appropriate box.. For example, an edge with cost = 28 is inserted into the box with interval 26.1 – 33). A box is empty if there is no edge in the graph whose value is within the interval of the box.
6. Sort all edges within the boxes into min heaps.
7. At the first box (box with the lowest interval), remove the minimum edge (the root of the heap) and place it back in the graph.
8. Take the edge that is now on the top and add it to the spanning tree if it does not form a cycle, else, discard that edge. Repeat this until the heap is empty or the minimum spanning tree has been formed.
9. If the minimum spanning tree has not been established yet, move to the next box and repeat step 7 & 8 until the last box, or until the minimum spanning tree has been formed.

## Reason for modification
The modified Kruskal algorithm has been shown to improve run times by an average of 16%. This would have a massive impact on efficiency if the size of the graph was large. 
