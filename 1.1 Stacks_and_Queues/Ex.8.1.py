from collections import deque

END_COMMAND = 'END'
GREEN_COMMAND = 'green'

green_light = int(input())
free_window = int(input())

cars = deque()
n = 0
flag = False
car_hit = ''
while True:
    line = input()
    if line == END_COMMAND:
        break
    elif line == GREEN_COMMAND:
        i = 0
        while i < green_light:
            if cars:
                current_car = cars.popleft()
                if green_light - i < len(current_car):
                    cars.appendleft(current_car[green_light - i:])
                    flag = True
                    car_hit = current_car
                    break
                else:
                    n += 1
                    i += len(current_car)
            else:
                break
        i = 0
        if flag:
            current_car = cars.popleft()
            if free_window < len(current_car):
                print('A crash happened!')
                print(f'{car_hit} was hit at {current_car[free_window - i]}.')
                exit()
            else:
                flag = False
                n += 1
                break
    else:
        cars.append(line)

print('Everyone is safe.')
print(f'{n} total cars passed the crossroads.')
