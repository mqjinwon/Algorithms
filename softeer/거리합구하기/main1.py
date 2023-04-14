
import heapq
N = int(input())

# 그래프 정의
graph = [[]for _ in range(N+1)]

for i in range(N-1):
    x, y, t = map(int, input().split())

    # 주의!! 양방향이므로 두번 추가해아한다.
    graph[x].append([t, y])
    graph[y].append([t, x])

INF = 1e8


def dijkstra(q, init_node):

    shortest_length = [INF] * (N+1)
    shortest_length[init_node] = 0

    while q:
        length, start_node = heapq.heappop(q)

        if shortest_length[start_node] < length:
            continue

        for next_length, next_node in graph[start_node]:
            if shortest_length[next_node] > length + next_length:
                shortest_length[next_node] = length + next_length
                heapq.heappush(q, [shortest_length[next_node], next_node])

    return shortest_length


# 결과 값
result = [0] * (N+1)

for node_idx in range(1, N+1):

    # 기본 변수 정의

    # 여기서 다익스트라 알고리즘으로 최단거리를 구해야한다.
    q = []
    heapq.heappush(q, [0, node_idx])

    shortest_length = dijkstra(q, node_idx)

    # 최종적으로 계산된 거리의 합을 result에 더함
    result[node_idx] = sum(shortest_length[1:])

# 결과물 출력
for idx in range(1, N+1):
    print(result[idx])
