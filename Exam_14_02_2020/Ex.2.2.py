PLAYER_SYMBOL = "P"
WALL_SYMBOL = 'X'

def in_range(row, col, n):
    if 0 <= row < n and 0 <= col < n:
        return True
    return False


def get_next_position(command, row_index, col_index):
    next_row_position = row_index
    next_col_position = col_index
    if command == "up":
        next_row_position = row_index-1
        next_col_position = col_index
    elif command == "down":
        next_row_position = row_index+1
        next_col_position = col_index
    elif command == "left":
        next_row_position = row_index
        next_col_position = col_index-1
    elif command == "right":
        next_row_position = row_index
        next_col_position = col_index+1

    return next_row_position, next_col_position


def get_walls_position(matrix):
    walls_position = []
    for row_index in range(len(matrix)):
        if WALL_SYMBOL in matrix[row_index]:
            column_index = matrix[row_index].index(WALL_SYMBOL)
            walls_position.append((row_index, column_index))
    return walls_position



def get_player_position(matrix):
   for row_index in range(len(matrix)):
    if PLAYER_SYMBOL in matrix[row_index]:
        column_index = matrix[row_index].index(PLAYER_SYMBOL)
        return [row_index, column_index]


def read_matrix():
    matrix = []
    for _ in range(n):
        matrix.append(input().split())
    return matrix


n = int(input())
matrix = read_matrix()
player_row, player_col = get_player_position(matrix)
walls = get_walls_position(matrix)


moves = []
coins = 0
while True:
    command = input()
    row, col = get_next_position(command, player_row, player_col)
    player_row = row
    player_col = col

    try:
        if matrix[row][col] == WALL_SYMBOL or not in_range(row, col, n):
            coins = coins // 2
            # moves.append([row, col])
            print(f"Game over! You've collected {coins} coins.")
            break
        else:
            moves.append([row, col])
            new_coin = int(matrix[row][col])
            coins += new_coin
            if coins >= 100:
                print(f"You won! You've collected {coins} coins.")
                break
    except:
        coins = coins // 2
            # moves.append([row, col])
        print(f"Game over! You've collected {coins} coins.")
        break


print("Your path:")
for el in moves:
    print(el)
