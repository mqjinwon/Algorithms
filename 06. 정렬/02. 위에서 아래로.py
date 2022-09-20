# It takes 1 minutes 41 seconds
# 3
# 15
# 27
# 12

N = int(input())

array = []

for _ in range(N):
    array.append(int(input()))

array.sort(reverse=True)

print(array)


