# stuff num, max weight
N, K = map(int, input().split())

# weight, value
stuffs = [list(map(int, input().split())) for _ in range(N)]

# 인덱스를 맞춰주기 위해 1개씩 더 더한다.
dp = [[0] * (K+1) for _ in range(N+1)]

# 물건이 하나도 없는 상황 가치는 0
for i in range(N+1):
    dp[i][0] = 0
# 무게가 0인 물건은 없기에, 0으로 초기화
for i in range(K+1):
    dp[0][i] = 0

for n in range(1, N+1):
    for w in range(1, K+1):

        # 물건을 실을 수 없으면, 이전의 dp값을 가져와 저장한다.ㅁ
        if stuffs[n-1][0] > w:
            dp[n][w] = dp[n-1][w]
        else:
            # 가치를 비교한다. 이전의 가치 vs 물건을 넣기전 가지고 있던 가치 + 넣었을 때 가치
            dp[n][w] = max(dp[n-1][w], dp[n-1]
                           [w-stuffs[n-1][0]] + stuffs[n-1][1])

print(dp[N][K])
