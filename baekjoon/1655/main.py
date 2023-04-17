import sys
import heapq

small_heap = []
large_heap = []

n = int(sys.stdin.readline())

for _ in range(n):
    num = int(sys.stdin.readline())

    if len(small_heap) == len(large_heap):
        heapq.heappush(small_heap, -num)
    else:
        heapq.heappush(large_heap, num)

    if len(large_heap) > 0:
        if -small_heap[0] > large_heap[0]:
            small = heapq.heappop(small_heap)
            large = heapq.heappop(large_heap)

            heapq.heappush(small_heap, -large)
            heapq.heappush(large_heap, -small)

    print(-small_heap[0])
