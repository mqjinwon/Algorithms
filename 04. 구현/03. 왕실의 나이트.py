# It takes 15 minutes 2 seconds

knight_pos = input()

map_size = 8

row = [ str(i+1) for i in range(map_size)]
col = [ chr(i+97) for i in range(map_size)]

print(row, col)

index = [row.index(knight_pos[1])+1, col.index(knight_pos[0])+1]

move_list = [(2, 1), (2, -1), (-2, 1), (-2, -1), 
            (1, 2), (1, -2), (-1, 2), (-1, -2)]

count = 0
for move in move_list:
    after_move_pos_row = index[0] + move[0]
    after_move_pos_col = index[1] + move[1]

    if 1 <= after_move_pos_row <= 8 and 1 <= after_move_pos_col <= 8:
        count += 1


print(count)