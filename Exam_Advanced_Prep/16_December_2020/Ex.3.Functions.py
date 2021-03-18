def get_magic_triangle(n):
    row = [1]
    y = [0]
    triangle_a = []
    triangle_a.append(row)

    for x in range(n - 1):
        row = [left + right for left, right in zip(row + y, y + row)]
        triangle_a.append(row)
    return triangle_a


print(get_magic_triangle(5))
