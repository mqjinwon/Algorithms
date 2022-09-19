# It takes 27 minutes 3 seconds
# 4 4
# 1 1 0
# 1 1 1 1 
# 1 0 0 1
# 1 1 0 1
# 1 1 1 1

# 북 동 남 서
# 0, 1, 2, 3

def move(direction):
    if direction == 0:
        return [-1, 0]
    elif direction == 1:
        return [0, 1]
    elif direction == 2:
        return [1, 0]
    elif direction == 3:
        return [0, -1]

def rotate(angle):
    angle -= 1
    if angle < 0:
        angle = 3

    return angle


N,M = map(int, input().split())

row, col, direction = map(int, input().split())

map_list = []

for i in range(N):
    map_list.append(list(map(int, input().split())))

map_list[row][col] = 1

position = [row, col]
count = 1

rotation_time = 0

while True:

    direction = rotate(direction)
    moved_pos = [x+y for x,y in zip(position, move(direction))]
    # 내부의 맵이라면
    if 0 <= moved_pos[0] < N and 0 <= moved_pos[1] < M and map_list[moved_pos[0]][moved_pos[1]] == 0:
        map_list[position[0]][position[1]] = 1 # 갔던 곳은 1로 표시
        position = moved_pos # 실제로 움직이기
        count +=1
        rotation_time = 0
    # 바다라면
    else:
        rotation_time +=1

    # 네바퀴 다 돌았다면
    if rotation_time == 4:
        moved_pos = [x-y for x,y in zip(position, move(direction))]
        # 뒤로 갈 수 있다면
        if 0 <= moved_pos[0] < N and 0 <= moved_pos[1] < M and map_list[moved_pos[0]][moved_pos[1]] == 0:
            position = moved_pos
            count += 1
            rotation_time = 0
        # 뒤가 바다라면
        else:
            break

print(count)

