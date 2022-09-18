# It takes 23 minutes 18 seconds
# 5 8 3 
# 2 4 5 4 6 

N, M, K = map(int, input().split())

N_list = list(map(int, input().split()))

# N: 배열의 크기
# M: 숫자가 더해지는 횟수
# K: 인덱스당, 최대로 더해지는 횟수

assert len(N_list) == N
assert K <= M

# print(N, M, K)
# print(N_list)

N_list.sort(reverse=True)

result = 0

# naive 하게 푸는 방법 (느림...)
# count = 0
# while 1:
#     if count + K <= M:
#         result += N_list[0] * K
#         count += K
#         if count == M:
#             break

#         result += N_list[1]
#         count += 1

#         if count == M:
#             break

# 빠르게 푸는 방법
first = N_list[0]
second = N_list[1]

result += (M // (K + 1)) * (first * K + second)
result += (M % (K + 1)) * second

print(result)