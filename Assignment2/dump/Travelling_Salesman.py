import itertools

def travelling_salesman(graph, start):
    nodes = list(graph.keys())
    nodes.remove(start)
    shortest_path = None
    min_cost = float('inf')

    for perm in itertools.permutations(nodes):
        current_cost = 0
        current_path = [start] + list(perm) + [start]

        for i in range(len(current_path) - 1):
            current_cost += graph[current_path[i]][current_path[i + 1]]

        if current_cost < min_cost:
            min_cost = current_cost
            shortest_path = current_path

    return shortest_path, min_cost


graph = {
    'A': {'A': 0, 'B': 10, 'C': 15, 'D': 20},
    'B': {'A': 10, 'B': 0, 'C': 35, 'D': 25},
    'C': {'A': 15, 'B': 35, 'C': 0, 'D': 30},
    'D': {'A': 20, 'B': 25, 'C': 30, 'D': 0}
}

path, cost = travelling_salesman(graph, 'A')

print("Shortest Path:", " -> ".join(path))
print("Minimum Cost:", cost)