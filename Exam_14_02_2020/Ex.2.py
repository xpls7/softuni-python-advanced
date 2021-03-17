

PLAYER_SYMBOL = "P"

def check_valid_position(row, col, matrix):
    if 0 <= row <= len(matrix) and 0 <= col <= len(matrix):
        return True
    return False

def check_next_position(row, col, matrix):
    if check_valid_position(row, col, matrix):
        next_position = matrix[row][col]
        return next_position
    return "X"

def get_walls_position(matrix):
    walls_position = []
    for row_index in range(len(matrix)):
        if PLAYER_SYMBOL in matrix[row_index]:
            column_index = matrix[row_index].index(PLAYER_SYMBOL)
            walls_position.append([row_index, column_index])
    return walls_position

def get_player_position(matrix):
   for row_index in range(len(matrix)):
    if PLAYER_SYMBOL in matrix[row_index]:
        column_index = matrix[row_index].index(PLAYER_SYMBOL)
        return [row_index, column_index]



size = int(input())

matrix = []
for _ in range(size):
    matrix.append(input().split())

row_index, col_index = get_player_position(matrix)
walls = get_walls_position(matrix)


coins = 0
while True:
    command = input()
    if command == "up":
        next_row_position = row_index-1
        next_col_position = col_index
        next_position = check_next_position(next_row_position, next_col_position, matrix)
        if next_position == "X":
            coins = coins // 2
            print(f"Game over! You've collected {coins} coins.")
            break
        else:
            next_position = int(next_position)
            coins += next_position
            if coins >= 100:
                print(f"You won! You've collected {coins} coins.")


    elif command == "down":
        next_row_position = row_index+1
        next_col_position = col_index
        next_position = check_next_position(next_row_position, next_col_position, matrix)
        if next_position == "X":
            coins = coins // 2
            print(f"Game over! You've collected {coins} coins.")
            break
        else:
            next_position = int(next_position)
            coins += next_position
            if coins >= 100:
                print(f"You won! You've collected {coins} coins.")

    elif command == "left":
        next_row_position = row_index
        next_col_position = col_index-1
        next_position = check_next_position(next_row_position, next_col_position, matrix)
        if next_position == "X":
            coins = coins // 2
            print(f"Game over! You've collected {coins} coins.")
            break
        else:
            next_position = int(next_position)
            coins += next_position
            if coins >= 100:
                print(f"You won! You've collected {coins} coins.")


    elif command == "right":
        next_row_position = row_index
        next_col_position = col_index+1
        next_position = check_next_position(next_row_position, next_col_position, matrix)
        if next_position == "X":
            coins = coins // 2
            print(f"Game over! You've collected {coins} coins.")
            break
        else:
            next_position = int(next_position)
            coins += next_position
            if coins >= 100:
                print(f"You won! You've collected {coins} coins.")
