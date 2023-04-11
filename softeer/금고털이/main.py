
W, N = map(int, input().split())

rock = [list(map(int, input().split())) for _ in range(N)]

# 오름차순으로 정렬한다.
sorted_rock = sorted(rock, key=lambda x: x[1], reverse=True)

result = 0

for i in range(N):
    # 값이 많이 나가는 것부터 하나씩 채워나간다.
    if sorted_rock[i][0] <= W:
        result += sorted_rock[i][0] * sorted_rock[i][1]
        W -= sorted_rock[i][0]
    else:
        result += W * sorted_rock[i][1]
        break

print(result)
