import heapq

def a_star(graph, heuristics, start, goal):
    open_list = [(heuristics[start], 0, start, [start])]  # (f, g, node, path)
    closed = set()

    while open_list:
        f, g, node, path = heapq.heappop(open_list)

        if node == goal:
            return path, g

        if node in closed:
            continue

        closed.add(node)

        for neighbor, cost in graph[node].items():
            if neighbor not in closed:
                g_new = g + cost
                f_new = g_new + heuristics[neighbor]
                heapq.heappush(open_list, (f_new, g_new, neighbor, path + [neighbor]))

    return None, float('inf')


graph_astar = {
    'A': {'B': 1, 'C': 3},
    'B': {'D': 3, 'E': 1},
    'C': {'F': 5},
    'D': {},
    'E': {'G': 2},
    'F': {'G': 2},
    'G': {}
}

heuristics = {'A': 7, 'B': 6, 'C': 5, 'D': 4, 'E': 2, 'F': 1, 'G': 0}

path, cost = a_star(graph_astar, heuristics, 'A', 'G')
print("A* Shortest Path:", path, "with cost", cost)


class AONode:
    def __init__(self, name):
        self.name = name
        self.children = []  # (list of alternatives, each alternative is a list of nodes)
        self.cost = float('inf')
        self.solved = False
        self.best_child = None


def ao_star(node, graph, heuristic):
    if node.solved:
        return node.cost

    if not graph.get(node.name):
        node.cost = heuristic.get(node.name, 0)
        node.solved = True
        return node.cost

    min_cost = float('inf')
    best_child = None

    for alternative in graph[node.name]:
        cost = 0
        for child, weight in alternative:
            child_node = AONode(child)
            cost += weight + ao_star(child_node, graph, heuristic)

        if cost < min_cost:
            min_cost = cost
            best_child = alternative

    node.cost = min_cost
    node.best_child = best_child
    node.solved = True
    return node.cost


def print_solution(node):
    if node.best_child:
        print(f"{node.name} -> {[child for child, _ in node.best_child]}")
        for child, _ in node.best_child:
            print_solution(AONode(child))


graph_aostar = {
    'A': [[('B', 1), ('C', 1)], [('D', 1)]],  # A can go to (B AND C) or D
    'B': [[('E', 1)]],
    'C': [[('F', 1)]],
    'D': [[('G', 1)]],
    'E': [],
    'F': [],
    'G': []
}

heuristic_aostar = {'A': 3, 'B': 2, 'C': 2, 'D': 1, 'E': 0, 'F': 0, 'G': 0}

root = AONode('A')
print("\nAO* Algorithm:")
total_cost = ao_star(root, graph_aostar, heuristic_aostar)
print("Total Cost from root:", total_cost)
print("Solution Path:")
print_solution(root)