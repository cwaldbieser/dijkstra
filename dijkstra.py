#! /usr/bin/env python

import heapq as heap
import sys
from collections import defaultdict


def dijkstra(G, starting_node):
    """
    Dijkstra's shortest path algorithm.
    Given `G`, a graph and a `starting_node`, return a
    (`parents_map`, `node_costs`).
    G should be an adjacentcy matrix such that G[node0][node1] produces the
    distance from node0 to node1.
    """
    visited = set()
    parents_map = {}
    pq = []
    node_costs = defaultdict(lambda: float("inf"))
    node_costs[starting_node] = 0
    heap.heappush(pq, (0, starting_node))

    while pq:
        # go greedily by always extending the shorter cost nodes first
        _, node = heap.heappop(pq)
        visited.add(node)

        for adj_node, weight in enumerate(G[node]):
            if adj_node in visited:
                continue

            newCost = node_costs[node] + weight
            if node_costs[adj_node] > newCost:
                parents_map[adj_node] = node
                node_costs[adj_node] = newCost
                heap.heappush(pq, (newCost, adj_node))

    return parents_map, node_costs


def get_path(parent_map, start, end):
    """
    Return the path from start to end.
    """
    path = []
    node = end
    while node != start:
        path.append(node)
        node = parent_map[node]
    path.append(start)
    path.reverse()
    return path


def example():
    """
    An example of finding the shortest path.
    """
    node_count = 7
    adjacency_matrix = [[sys.maxsize] * node_count for _ in range(node_count)]
    adjacency_matrix[0][1] = 2
    adjacency_matrix[0][2] = 6
    adjacency_matrix[1][0] = 2
    adjacency_matrix[1][3] = 5
    adjacency_matrix[2][0] = 6
    adjacency_matrix[2][3] = 8
    adjacency_matrix[3][1] = 5
    adjacency_matrix[3][2] = 8
    adjacency_matrix[3][4] = 10
    adjacency_matrix[3][5] = 15
    adjacency_matrix[4][3] = 10
    adjacency_matrix[4][5] = 6
    adjacency_matrix[4][6] = 2
    adjacency_matrix[5][3] = 15
    adjacency_matrix[5][4] = 6
    adjacency_matrix[5][6] = 6
    adjacency_matrix[6][4] = 2
    adjacency_matrix[6][5] = 6
    parents_map, node_costs = dijkstra(adjacency_matrix, 0)
    print("Adjacency matrix:")
    print(" ", end="")
    print("".join("{:3d} ".format(n) for n in range(node_count)))
    print("----" * node_count + "-")
    for j, row in enumerate(adjacency_matrix):
        fmt_row = []
        for item in row:
            if item == sys.maxsize:
                fmt_row.append("   ")
            else:
                fmt_row.append("{:3d}".format(item))
        print("|", end="")
        print("|".join(fmt_row), end="")
        print("| {:3d}".format(j))
        print("----" * node_count + "-")
    print("")
    for n in range(node_count):
        path = get_path(parents_map, 0, n)
        pathstr = " -> ".join(str(n) for n in path)
        print(
            "Shortest path from node 0 to node {}: {:3d}; {}".format(
                n, node_costs[n], pathstr
            )
        )


if __name__ == "__main__":
    example()
