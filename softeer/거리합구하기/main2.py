N = int(input())

INF = 1e8
graph = [[INF]*(N+1) for _ in range(N+1)]

# 그래프 정의
for i in range(N-1):
    x, y, t = map(int, input().split())
    graph[x][y] = t
    graph[y][x] = t

# 자기자신은 0으로 초기화
for i in range(1, N+1):
    graph[i][i] = 0

# floyd-warshall 알고리즘
for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(1, N+1):
    print(sum(graph[i][1:]))
