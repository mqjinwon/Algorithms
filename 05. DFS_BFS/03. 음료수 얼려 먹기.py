# It takes 9 minutes 23 seconds

# 4 5
# 00110
# 00011
# 11111
# 00000

N, M = map(int, input().split())

ice_map = []
for i in range(N):
    ice_map.append([int(j) for j in input()])

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(x,y, ice_map):
    ice_map[x][y] = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        if ice_map[nx][ny] == 0:
            dfs(nx, ny, ice_map)

count =0

for i in range(N):
    for j in range(M):
        if ice_map[i][j] == 0:
            dfs(i, j, ice_map)
            count += 1

print(count)