from collections import deque

def water_jug_problem(capacity1, capacity2, target):
    visited = set()
    parent = {}  # to reconstruct path

    def get_next_states(x, y):
        return [
            (capacity1, y),  # Fill jug1
            (x, capacity2),  # Fill jug2
            (0, y),          # Empty jug1
            (x, 0),          # Empty jug2
            # Pour jug2 → jug1
            (min(x + y, capacity1), y - (min(x + y, capacity1) - x)),
            # Pour jug1 → jug2
            (x - (min(x + y, capacity2) - y), min(x + y, capacity2))
        ]

    # BFS queue
    queue = deque([(0, 0)])
    visited.add((0, 0))

    while queue:
        state = queue.popleft()
        if state == target:
            # reconstruct path
            path = []
            while state in parent:
                path.append(state)
                state = parent[state]
            path.append((0, 0))
            path.reverse()
            return path

        for next_state in get_next_states(*state):
            if next_state not in visited:
                visited.add(next_state)
                parent[next_state] = state
                queue.append(next_state)

    return None


# -----------------------------
# Static Example
# -----------------------------
print("WATER JUG PROBLEM (BFS version)")
capacity1 = 4   # Jug1 capacity
capacity2 = 3   # Jug2 capacity
target = (2, 0)  # Goal: 2L in Jug1, 0L in Jug2

solution = water_jug_problem(capacity1, capacity2, target)

if solution:
    print("Steps to reach the target:")
    for s in solution:
        print(f"Jug1: {s[0]}L , Jug2: {s[1]}L")
else:
    print("No solution found.")