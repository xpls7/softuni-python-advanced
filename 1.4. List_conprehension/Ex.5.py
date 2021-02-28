size = int(input())

matrix = []
for row in range(size):
    matrix.append([int(el) for el in input().split(", ")])

primary_diagonal = []
secondary_diagonal = []

for i in range(len(matrix)):
    for j in range(len(matrix)):
        if i == j:
            primary_diagonal.append(matrix[i][j])
        if (i+j) == len(matrix)-1:
            secondary_diagonal.append(matrix[i][j])

print(f"First diagonal: {', '.join(map(str, primary_diagonal))}. Sum: {sum(primary_diagonal)}")
print(f"Second diagonal: {', '.join(map(str, secondary_diagonal))}. Sum: {sum(secondary_diagonal)}")



