rows, cols = [int(el) for el in input().split()]

def init_matrix():
    matrix = []

    for _ in range(rows):
        matrix.append([int(el) for el in input().split()])

    return matrix


def max_sum(row, col, matr):
    row_1 = matr[row][col] + matr[row][col+1] + matr[row][col+2]
    row_2 = matr[row+1][col] + matr[row+1][col+1] + matr[row+1][col+2]
    row_3 = matr[row+2][col] + matr[row+2][col+1] + matr[row+2][col+2]

    matrix_sum = row_1 + row_2 + row_3
    current_row = row
    current_col = col

    return matrix_sum, current_row, current_col

matrix = init_matrix()

result = 0
best_sum = -999999999999999999
r_1 = []
r_2 = []
r_3 = []
for row_index in range(rows-2):
    for col_index in range(cols-2):
        current_sum, current_r, current_c = max_sum(row_index, col_index, matrix)
        if current_sum > best_sum:
            best_sum = current_sum
            best_r = current_r
            best_c = current_c

print(f"Sum = {best_sum}")
print(f"{matrix[best_r][best_c]} {matrix[best_r][best_c+1]} {matrix[best_r][best_c+2]}")
print(f"{matrix[best_r+1][best_c]} {matrix[best_r+1][best_c+1]} {matrix[best_r+1][best_c+2]}")
print(f"{matrix[best_r+2][best_c]} {matrix[best_r+2][best_c+1]} {matrix[best_r+2][best_c+2]}")

