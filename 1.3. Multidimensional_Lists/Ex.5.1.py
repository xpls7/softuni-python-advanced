rows, cols = [int(el) for el in input().split()]

word = input()

matrix = []

for row_index in range(rows):
    matrix.append([0 for el in range(cols)])

index_word = 0

for row_index in range(rows):
    if row_index % 2 == 1:
        for col_index in range(cols-1, -1, -1): # запълва реда отзад напред
            matrix[row_index][col_index] = word[index_word]
            index_word += 1
            if index_word == len(word):
                index_word = 0
    else:
        for col_index in range(cols):  # запълва реда започвайки отначало
            matrix[row_index][col_index] = word[index_word]
            index_word += 1
            if index_word == len(word):
                index_word = 0

for row_index in range(rows):
    if row_index % 2 == 1:
        matrix[row_index].reverse()
    print("".join(matrix[row_index]))
