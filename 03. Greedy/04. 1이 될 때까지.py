# It takes 10 minutes 36 seconds
N, K = map(int, input().split())

# 1. N을 1로 뺀다.
# 2. N을 K로 나눈다.

# 얼마나 자주 나눌 수 있으냐가 관건...
count = 0
while N != 0:
    while N % K == 0:
        N = N / K
        count += 1

    reminder = int(N % K)
    N -= reminder
    count += reminder

# N을 0까지 만들었기 때문에...
count -= 1

print(count)
