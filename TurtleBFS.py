import turtle
import time
from collections import deque

grid = [
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [1, 1, 0, 1, 0, 1, 0, 1, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 1, 0, 0, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 1, 0, 0, 1, 0, 0],
    [0, 1, 0, 1, 0, 1, 0, 1, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 1, 1, 1, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 0, 0, 0]
]

start = (0, 0)
goal = (9, 9)
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

cell_size = 30
rows, cols = 10, 10

screen = turtle.Screen()
screen.title("BFS Grid Navigation Visualization (10x10)")
screen.setup(width=700, height=700)
screen.tracer(0)

pen = turtle.Turtle()
pen.speed(0)
pen.penup()
pen.hideturtle()

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

def draw_grid():
    for i in range(rows):
        for j in range(cols):
            color = "white" if grid[i][j] == 0 else "black"
            draw_cell(i, j, color)
    screen.update()

draw_grid()

def to_screen(x, y):
    return y * cell_size - (cols * cell_size / 2) + cell_size / 2, -(x * cell_size - (rows * cell_size / 2)) - cell_size / 2

def bfs_visual(start, goal):
    queue = deque([[start]])
    visited = set([start])
    nodes_expanded = 0

    while queue:
        path = queue.popleft()
        x, y = path[-1]
        nodes_expanded += 1

        if (x, y) != start and (x, y) != goal:
            draw_cell(x, y, "lightgray")
            screen.update()
            time.sleep(0.1)

        if (x, y) == goal:
            for (px, py) in path:
                if (px, py) not in [start, goal]:
                    draw_cell(px, py, "deepskyblue")
                    screen.update()
                    time.sleep(0.1)
            return path, nodes_expanded

        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0 and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append(path + [(nx, ny)])
    return None, nodes_expanded

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
