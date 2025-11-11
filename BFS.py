from collections import deque

grid = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0]
]

start = (0, 0)
goal = (4, 4)

moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def is_valid(x, y):
    return 0 <= x < 5 and 0 <= y < 5 and grid[x][y] == 0

def bfs(start, goal):
    queue = deque([[start]])
    visited = set([start])
    nodes_expanded = 0

    while queue:
        path = queue.popleft()
        x, y = path[-1]
        nodes_expanded += 1

        if (x, y) == goal:
            return path, nodes_expanded

        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny) and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append(path + [(nx, ny)])
    
    return None, nodes_expanded

path, expanded = bfs(start, goal)

print("\n--- BFS Algorithm Results ---")
if path:
    print("Path Found: YES")
    print("Path Length (Steps):", len(path) - 1)
    print("Nodes Expanded (Time Proxy):", expanded)
    print("Full Path:", path)
else:
    print("Path Found: NO")

print("\n--- Final Map ---")
for i in range(5):
    for j in range(5):
        if (i, j) == start:
            print("S", end="")
        elif (i, j) == goal:
            print("G", end="")
        elif (i, j) in path[1:-1]:
            print("*", end="")
        elif grid[i][j] == 1:
            print("#", end="")
        else:
            print(".", end="")
    print()