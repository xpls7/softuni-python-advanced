from collections import deque

fireworks_effects = deque([int(el) for el in input().split(", ")])
explosive_power = [int(el) for el in input().split(", ")]

fireworks_effects_count = 0
explosive_power_count = 0

palm_firework = 0
willow_firework = 0
crossette_firework = 0

is_prepared = False


while fireworks_effects or explosive_power:
    try:
        current_firework_effect = fireworks_effects[0]
        current_explosive_power = explosive_power[-1]

        if current_firework_effect <= 0:
            fireworks_effects.popleft()
            continue
        if current_explosive_power <= 0:
            explosive_power.pop()
            continue

        result = current_explosive_power + current_firework_effect
        if result % 3 == 0 and result % 5 == 0:
            fireworks_effects.popleft()
            explosive_power.pop()
            crossette_firework += 1
        elif result % 3 == 0 and result % 5 != 0:
            fireworks_effects.popleft()
            explosive_power.pop()
            palm_firework += 1
        elif result % 5 == 0 and result % 3 != 0:
            fireworks_effects.popleft()
            explosive_power.pop()
            willow_firework += 1

        else:
            current_firework_effect -= 1
            fireworks_effects.popleft()
            fireworks_effects.append(current_firework_effect)


        if palm_firework >= 3 and willow_firework >= 3 and crossette_firework >= 3:
            is_prepared = True
            break
    except:
        if palm_firework >= 3 and willow_firework >= 3 and crossette_firework >= 3:
            is_prepared = True
            break
        else:
            break

if is_prepared:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can’t make the perfect firework show.")

if fireworks_effects:
    print(f"Firework Effects left: {', '.join(map(str, fireworks_effects))}")
if explosive_power:
    print(f"Explosive Power left: {', '.join(map(str, explosive_power))}")
print(f"Palm Fireworks: {palm_firework}")
print(f"Willow Fireworks: {willow_firework}")
print(f"Crossette Fireworks: {crossette_firework}")

