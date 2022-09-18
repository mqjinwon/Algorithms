#It takes about 8 minutes
## test set
# 3 3
# 3 1 2
# 4 1 4
# 2 2 2

# 2 4
# 7 3 1 8
# 3 3 3 4

N, M = map(int, input().split())

cards = list()

# 처음에 짠 버전
# for _ in range(N):
#     card_row = list(map(int, input().split()))
#     card_row.sort()
#     cards.append(card_row)

# max_card = 0

# for card_row in cards:
#     if card_row[0] > max_card:
#         max_card = card_row[0]

# 좀 더 간결한 버전
for _ in range(N):
    card_row = list(map(int, input().split()))
    cards.append(min(card_row))

max_card = max(cards)

print(max_card)
