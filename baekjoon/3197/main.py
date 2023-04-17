import sys
from collections import deque

input = sys.stdin.readline

# Get data
R, C = map(int, input().split())

# '.': water 'X': ice 'L': 백조
map_data = [list(input()) for _ in range(R)]

swan_pose = [0, 0]

find_flag = False
for r in range(R):
    for c in range(C):
        if map_data[r][c] == 'L':
            swan_pose = [r, c]
            find_flag = True

        if find_flag:
            break
    if find_flag:
        break

# for testing to check whether data come good.
# print(map_data)
# print(swan_pose)

drow = [0, 1, 0, -1]
dcol = [1, 0, -1, 0]


def check_boundary(row, col):
    if row < 0 or row >= R or col < 0 or col >= C:
        return False
    else:
        return True


def swan_bfs(q):

    visited = [[False]*C for _ in range(R)]

    while (q):
        r, c = q.popleft()
        visited[r][c] = True

        for i in range(4):
            moved_r = r + drow[i]
            moved_c = c + dcol[i]

            if check_boundary(moved_r, moved_c):
                # already visited before
                if visited[moved_r][moved_c]:
                    continue
                else:
                    if map_data[moved_r][moved_c] == "L":
                        return True
                    elif map_data[moved_r][moved_c] == "X":
                        continue
                    else:
                        q.append([moved_r, moved_c])

    return False


def melt_bfs(q, visited):
    while (q):
        r, c = q.popleft()
        visited[r][c] = True

        for i in range(4):
            moved_r = r + drow[i]
            moved_c = c + dcol[i]

            if check_boundary(moved_r, moved_c):
                # already visited before
                if visited[moved_r][moved_c]:
                    continue
                else:
                    if map_data[moved_r][moved_c] == "L":
                        q.append([moved_r, moved_c])
                    elif map_data[moved_r][moved_c] == "X":
                        map_data[moved_r][moved_c] = "."
                        visited[moved_r][moved_c] = True
                    else:
                        q.append([moved_r, moved_c])


step = 0

while (True):
    # check whether swan can meet together
    swan_q = deque([swan_pose])
    meet_flag = swan_bfs(swan_q)

    if meet_flag:
        break

    # if swan can't meet together, melt ice
    step += 1

    water_visited = [[False]*C for _ in range(R)]
    for r in range(R):
        for c in range(C):
            # place is water and not visited yet
            if map_data[r][c] == "." and water_visited[r][c] == False:
                water_q = deque([[r, c]])
                melt_bfs(water_q, water_visited)

print(step)
