size = int(input())
matrix = []
for _ in range(size):
    matrix.append([int(el) for el in input().split()])

data = input()

while not data == "END":
    try:
        data = data.split()
        command = data[0]
        row = int(data[1])
        col = int(data[2])
        value = int(data[3])
        if 0 <= row < size and 0 <= col < size:
            if command == "Add":
                matrix[row][col] += value
            elif command == "Subtract":
                matrix[row][col] -= value
            else:
                print("Invalid coordinates")
        else:
            print("Invalid coordinates")
    except:
        print("Invalid coordinates")

    data = input()

for row in matrix:
    print(" ".join(map(str, row)))
