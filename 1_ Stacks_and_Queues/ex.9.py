from collections import deque

bullet_price = int(input())
gun_barrel_size = int(input())
bullets = [int(el) for el in input().split()]
locks = deque([int(el) for el in input().split()])
intelligence = int(input())

reloading = deque([])
is_bullets = False

bullets_used = 0
money_earned = 0


if gun_barrel_size >= 0:
    gun_barrel_size -= 1
    for lock in locks:
            gun_barrel_size -= 1
            if lock >= bullets[-1]:
                bullets.pop()
                locks.popleft()
                print("Bang!")
                if bullets:
                    print("Reloading!")
            else:
                bullets.pop()
                bullets_used += 1
                print("Ping!")
                if bullets:
                    print("Reloading!")

bullets_cost = bullets_used * bullet_price
money_earned = intelligence - bullets_cost


if bullets:
    print(f"Couldn't get through. Locks left: {len(locks)}")
else:
    print(f"{len(bullets)} bullets left. Earned {money_earned}")
