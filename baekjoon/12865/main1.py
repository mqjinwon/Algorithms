N, K = map(int, input().split())

# weight, value
stuffs = [list(map(int, input().split())) for _ in range(N)]

# 무게당 가치 구하기
for stuff in stuffs:
    stuff.append(stuff[1]/stuff[0])

# 무게당 가치 내림차순, 무게 오름차순
stuffs = sorted(stuffs, key=lambda x: (-x[-1], x[0]))

results = []


for idx in range(N):
    weight = K
    result = 0
    for stuff in stuffs[idx:]:
        if weight >= stuff[0]:
            weight -= stuff[0]
            result += stuff[1]
    results.append(result)

print(max(results))
