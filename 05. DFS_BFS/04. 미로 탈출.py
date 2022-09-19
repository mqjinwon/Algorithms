# It takes 17 minutes 30 seconds
# 5 6
# 101010
# 111111
# 000001
# 111111
# 111111


N, M = map(int, input().split())

maze_map = []
for i in range(N):
    maze_map.append(list(map(int, input())))

print(maze_map)

x = 1
y = 1

from collections import deque

def bfs(x, y, target_x, target_y, maze_map):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    queue = deque()
    queue.append((y, x))


    while queue:
        y, x = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 1 or nx > M or ny < 1 or ny > N:
                continue
            if maze_map[ny-1][nx-1] != 1:
                continue
            if maze_map[ny-1][nx-1] == 1:
                maze_map[ny-1][nx-1] += maze_map[y-1][x-1]
                queue.append((ny, nx))

                if nx == target_x and ny == target_y:
                    return maze_map[target_y-1][target_x-1]

print(bfs(x, y, M, N, maze_map))
