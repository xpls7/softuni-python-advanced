n = int(input())

territory = [list(input()) for _ in range(n)]


def search_matrix(matrix, search):
    for y, row in enumerate(matrix):
        for x, char in enumerate(row):
            if char == search:
                return y, x


def move(dy, dx):
    global snake_pos, game_over, food_quantity
    y, x = snake_pos
    territory[y][x] = '.'
    new_y = y + dy
    new_x = x + dx

    if new_y > (n - 1) or new_y < 0 or new_x > (n - 1) or new_x < 0:
        game_over = True
        return

    at_pos = territory[new_y][new_x]
    if at_pos == 'B':
        territory[new_y][new_x] = '.'
        new_y, new_x = search_matrix(territory, 'B')
    elif at_pos == '*':
        food_quantity += 1
        if food_quantity >= 10:
            game_over = True
    territory[new_y][new_x] = 'S'
    snake_pos = (new_y, new_x)


def print_territory():
    print('\n'.join([''.join(row) for row in territory]))


ops = {
    'up': lambda: move(-1, 0),
    'down': lambda: move(1, 0),
    'left': lambda: move(0, -1),
    'right': lambda: move(0, 1),
}


snake_pos = search_matrix(territory, 'S')
game_over = False
food_quantity = 0

while not game_over:
    command = input()
    move_fn = ops[command]
    move_fn()

if game_over and food_quantity < 10:
    print('Game over!')
else:
    print('You won! You fed the snake.')

print(f'Food eaten: {food_quantity}')
print_territory()





