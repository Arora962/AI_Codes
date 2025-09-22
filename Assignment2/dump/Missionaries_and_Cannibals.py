from collections import deque

start_state = (3, 3, 0, 0, 'L')
end_state = (0, 0, 3, 3, 'R')


boat_moves = [(1, 0), (0, 1), (2, 0), (0, 2), (1, 1)]


def is_valid(state):
    M_left, C_left, M_right, C_right, _ = state

    
    if M_left < 0 or C_left < 0 or M_right < 0 or C_right < 0:
        return False

    
    if M_left > 0 and C_left > M_left:
        return False

    
    if M_right > 0 and C_right > M_right:
        return False

    return True


def get_successors(state):
    successors = []
    M_left, C_left, M_right, C_right, boat = state

    for m, c in boat_moves:
        if boat == 'L':  
            new_state = (M_left - m, C_left - c,
                         M_right + m, C_right + c,
                         'R')
        else:  
            new_state = (M_left + m, C_left + c,
                         M_right - m, C_right - c,
                         'L')

        if is_valid(new_state):
            successors.append(new_state)

    return successors


def bfs(start, goal):
    queue = deque([(start, [start])])
    visited = set()

    while queue:
        state, path = queue.popleft()

        if state == goal:
            return path

        if state in visited:
            continue

        visited.add(state)

        for succ in get_successors(state):
            queue.append((succ, path + [succ]))

    return None


solution = bfs(start_state, end_state)

if solution:
    print("Solution found!")
    for step in solution:
        print(step)
else:
    print("No solution exists.")