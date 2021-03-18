from collections import deque

bomb_effects = deque([int(el) for el in input().split(", ")])
bomb_casings = [int(el) for el in input().split(", ")]

datura_bombs = 40
cherry_bombs = 60
smoke_decoy_bombs = 120

new_datura_bombs = []
new_cherry_bombs = []
new_smoke_decoy_bombs = []

while bomb_effects and bomb_casings:
    current_bomb_effect = bomb_effects.popleft()
    current_bomb_casing = bomb_casings.pop()
    current_sum = current_bomb_effect + current_bomb_casing
    if current_sum == datura_bombs:
        new_datura_bombs.append(current_sum)
    elif current_sum == cherry_bombs:
        new_cherry_bombs.append(current_sum)
    elif current_sum == smoke_decoy_bombs:
        new_smoke_decoy_bombs.append(current_sum)
    else:
        bomb_effects.appendleft(current_bomb_effect)
        current_bomb_casing -= 5
        if current_bomb_effect <= 0:
            if len(new_datura_bombs) >= 3 and len(new_cherry_bombs) >= 3 and len(new_smoke_decoy_bombs) >= 3:
                break
            continue
        else:
            bomb_casings.append(current_bomb_casing)

    if len(new_datura_bombs) >= 3 and len(new_cherry_bombs) >= 3 and len(new_smoke_decoy_bombs) >= 3:
        break

if len(new_datura_bombs) >= 3 and len(new_cherry_bombs) >= 3 and len(new_smoke_decoy_bombs) >= 3:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

if not bomb_effects:
    print("Bomb Effects: empty")
else:
    print(f"Bomb Effects: {', '.join(map(str, bomb_effects))}")
if not bomb_casings:
    print("Bomb Casings: empty")
else:
    print(f"Bomb Casings: {', '.join(map(str, bomb_casings))}")

print(f"Cherry Bombs: {len(new_cherry_bombs)}")
print(f"Datura Bombs: {len(new_datura_bombs)}")
print(f"Smoke Decoy Bombs: {len(new_smoke_decoy_bombs)}")
