# It takes 4 minutes 33 seconds


N = input()
N = int(N)

coin_list = [500, 100, 50, 10]

coin_num = 0

for coin in coin_list:
    while N >= coin:
        N -= coin
        coin_num += 1

if N == 0:
    print(coin_num)
else:
    print("There is some problem, check N has 10X values")