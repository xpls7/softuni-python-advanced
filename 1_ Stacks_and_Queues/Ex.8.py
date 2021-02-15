from collections import deque

green = int(input())
free = int(input())
command = input()
cars = deque()
total_passed = 0

time = green + free
no_crash = True

while command != 'END':
    if command == 'green':
        time = green + free

        while time >= 0:
            if cars and no_crash:
                current_car = cars.popleft()
                if len(current_car) <= time:
                    total_passed += 1
                    time -= len(current_car)
                    if time <= free:
                        time = 0
                        break
                else:
                    crash_site = current_car[time]
                    print('A crash happened!')
                    print(f'{current_car} was hit at {crash_site}.')
                    no_crash = False
                    break
            else:
                break
    else:
        cars.append(command)

    # print(time)
    # print(cars)

    command = input()

if no_crash:
    print('Everyone is safe.')
    print(f'{total_passed} total cars passed the crossroads.')
