def get_magic_triangle(n):
    matrix = []
    matrix.append([1])
    matrix.append([1, 1])

    def is_valid(n, m, i):
        if m < 0 or n < 0 or m > n:
            return 0
        try:
            wanted = matrix[n][m]
            return wanted
        except IndexError:
            return 0


    for i in range(2, n):
        row = []
        for j in range(i + 1):
           i1 = is_valid(i-1, j, i)
           j1 = is_valid(i-1, j-1, i)
           sum_val = i1 + j1
           row.append(sum_val)
        matrix.append(row)

    return matrix

print(get_magic_triangle(5))
