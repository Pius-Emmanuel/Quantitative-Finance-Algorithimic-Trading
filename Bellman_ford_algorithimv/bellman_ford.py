from collections import defaultdict

def bellman_ford(graph, source):
    # Initialize distance and predecessor arrays
    distance = defaultdict(lambda: float('inf'))
    predecessor = defaultdict(lambda: None)
    distance[source] = 0

    # Relax edges |V|-1 times
    for i in range(len(graph) - 1):
        for u, v, w in graph:
            if distance[u] + w < distance[v]:
                distance[v] = distance[u] + w
                predecessor[v] = u

    # Check for negative-weight cycles
    for u, v, w in graph:
        if distance[u] + w < distance[v]:
            raise ValueError("Graph contains a negative-weight cycle")

    return distance, predecessor

# Usage example:
graph = [
    (0, 1, -1),
    (0, 2, 4),
    (1, 2, 3),
    (1, 3, 2),
    (1, 4, 2),
    (3, 2, 5),
    (3, 1, 1),
    (4, 3, -3)
]

dist, pred = bellman_ford(graph, 0)

print("Vertex Distance Predecessor")
for i in range(len(graph)):
    print(i, "     ", dist[i], "      ", pred[i])

