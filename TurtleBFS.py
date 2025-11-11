import turtle
import time
from collections import deque

# ---------------- Grid Setup ----------------
grid = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 1, 0, 0, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 1, 0, 0]
]

start = (0, 0)
goal = (4, 4)
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right

# ---------------- BFS with Visualization ----------------
cell_size = 40
rows, cols = 5, 5

screen = turtle.Screen()
screen.title("BFS Grid Navigation Visualization")
screen.setup(width=500, height=500)
screen.tracer(0)

pen = turtle.Turtle()
pen.speed(0)
pen.penup()
pen.hideturtle()

# Draw a single cell
def draw_cell(i, j, color):
    x = j * cell_size - (cols * cell_size / 2)
    y = -(i * cell_size - (rows * cell_size / 2))
    pen.goto(x, y)
    pen.color("black", color)
    pen.begin_fill()
    for _ in range(4):
        pen.forward(cell_size)
        pen.right(90)
    pen.end_fill()

# Draw the static grid
def draw_grid():
    for i in range(rows):
        for j in range(cols):
            color = "white" if grid[i][j] == 0 else "black"
            draw_cell(i, j, color)
    screen.update()

draw_grid()

def to_screen(x, y):
    return y * cell_size - (cols * cell_size / 2) + cell_size / 2, -(x * cell_size - (rows * cell_size / 2)) - cell_size / 2

# BFS visualization
def bfs_visual(start, goal):
    queue = deque([[start]])
    visited = set([start])
    nodes_expanded = 0

    while queue:
        path = queue.popleft()
        x, y = path[-1]
        nodes_expanded += 1

        # visualize current node exploration
        if (x, y) != start and (x, y) != goal:
            draw_cell(x, y, "lightgray")
            screen.update()
            time.sleep(0.2)

        if (x, y) == goal:
            # Draw final path
            for (px, py) in path:
                if (px, py) not in [start, goal]:
                    draw_cell(px, py, "deepskyblue")
                    screen.update()
                    time.sleep(0.2)
            return path, nodes_expanded

        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 5 and 0 <= ny < 5 and grid[nx][ny] == 0 and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append(path + [(nx, ny)])
    return None, nodes_expanded

# mark start and goal
draw_cell(start[0], start[1], "green")
draw_cell(goal[0], goal[1], "red")
screen.update()

path, expanded = bfs_visual(start, goal)

print("\n--- BFS Algorithm Results ---")
if path:
    print("Path Found: YES")
    print("Path Length (Steps):", len(path) - 1)
    print("Nodes Expanded (Time Proxy):", expanded)
    print("Full Path:", path)
else:
    print("Path Found: NO")

turtle.done()
