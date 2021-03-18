import re

n = int(input())
bombs = int(input())


def check_cell_in_matrix(r, c, matrix_a):
    if 0 <= r <= len(matrix) and 0 <= c <= len(matrix):
        return True
    return False

def check_cell_for_star(r, c, matrix_b):
    try:
        if matrix_b[r][c] == "*":
            return True
        return False
    except IndexError:
        return False


def calculate_cell_size(matr):
    for row in range(len(matr)):
        for col in range(len(matr)):
            cell_size = 0
            if not matrix[row][col] == "*":

                if check_cell_for_star(row, col+1, matrix) and check_cell_in_matrix(row, col+1, matrix):
                    cell_size += 1
                if check_cell_for_star(row, col-1, matrix) and check_cell_in_matrix(row, col-1, matrix):
                    cell_size += 1
                if check_cell_for_star(row-1, col, matrix) and check_cell_in_matrix(row-1, col, matrix):
                    cell_size += 1
                if check_cell_for_star(row+1, col, matrix) and check_cell_in_matrix(row+1, col, matrix):
                    cell_size += 1
                if check_cell_for_star(row-1, col+1, matrix) and check_cell_in_matrix(row-1, col+1, matrix):
                    cell_size += 1
                if check_cell_for_star(row+1, col+1, matrix) and check_cell_in_matrix(row+1, col+1, matrix):
                    cell_size += 1
                if check_cell_for_star(row+1, col-1, matrix) and check_cell_in_matrix(row+1, col-1, matrix):
                    cell_size += 1
                if check_cell_for_star(row-1, col-1, matrix) and check_cell_in_matrix(row-1, col-1, matrix):
                    cell_size += 1
                matrix[row][col] = cell_size

    return matrix


def init_matrix(n):
    matrix = []
    for _ in range(n):
        matrix.append(list(0 for col in range(n)))
    return matrix


matrix = init_matrix(n)
for i in range(bombs):
    position = input()

    pattern = r'[0-9]+'

    numbers = re.findall(pattern, position)

    bomb_position_row = int(numbers[0])
    bomb_position_col = int(numbers[1])

    matrix[bomb_position_row][bomb_position_col] = "*"

final_matrix = calculate_cell_size(matrix)
for r in final_matrix:
    print(" ".join(map(str, r)))
