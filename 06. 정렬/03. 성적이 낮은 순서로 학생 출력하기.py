# It takes 3 minutes 49 seconds
# 2
# 홍길동 95
# 이순신 77

N = int(input())

array = list()

for _ in range(N):
    name, score = input().split()
    array.append([name, int(score)])


array.sort(key=lambda x: x[1])

for i in array:
    print(i[0], end=' ')