# It takes 12 minutes 44 seconds
# test set
# 5
# R R R U D D

map_size = int(input())
direction = list(map(str, input().split()))

position = [1, 1]

for dir in direction:
    if dir == 'L':  # 왼쪽
        if position[1] - 1 > 0:
            position[1] -= 1
    elif dir == 'R':  # 오른쪽
        if position[1] + 1 < map_size + 1:
            position[1] += 1
    elif dir == 'U':  # 위로
        if position[0] - 1 > 0:
            position[0] -= 1
    elif dir == 'D':  # 아래로
        if position[0] + 1 < map_size + 1:
            position[0] += 1

print(position[0], " ", position[1])
