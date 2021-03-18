from collections import deque

males = [int(el) for el in input().split()]
females = deque([int(el) for el in input().split()])

successful_matches = 0


while males and females:
        current_male = males[-1]
        current_female = females[0]
        if current_male <= 0:
            males.pop()
            continue
        elif current_female <= 0:
            females.popleft()
            continue
        elif current_male % 25 == 0:
            males.pop()
            continue
        elif current_female % 25 == 0:
            females.popleft()
            continue
        elif current_male == current_female:
            males.pop()
            females.popleft()
            successful_matches += 1
        else:
            females.popleft()
            males[-1] -= 2

print(f"Matches: {successful_matches}")
if males:
    print(f"Males left: {', '.join(str(el) for el in males[::-1])}")
else:
    print(f"Males left: none")
if females:
    print(f"Females left: {', '.join(map(str, females))}")
else:
    print(f"Females left: none")



