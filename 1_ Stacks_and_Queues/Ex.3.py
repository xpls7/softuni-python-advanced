from collections import deque

food_quantity = int(input())
order_quantity = deque(int(el) for el in input().split())

biggest_order = max(order_quantity)

while len(order_quantity) > 0:

    if food_quantity >= order_quantity[0]:
        food_quantity -= order_quantity[0]
        order_quantity.popleft()
    else:
        break


if not order_quantity and food_quantity >= 0:
    print(biggest_order)
    print("Orders complete")
else:
    print(biggest_order)
    print(f"Orders left: {' '.join(map(str, order_quantity))}")
