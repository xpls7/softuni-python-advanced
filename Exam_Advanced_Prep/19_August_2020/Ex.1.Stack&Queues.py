from collections import deque

customers = deque([int(el) for el in input().split(", ")])
taxis = [int(el) for el in input().split(", ")]


time = 0
if len(customers) >= 1 and len(taxis) >= 1:
    for i in range(len(taxis)):
        if taxis[-1] >= customers[0]:
            time += customers.popleft()
            taxis.pop()
        else:
            taxis.pop()
            if i > 0:
                i -= 1
            else:
                i = 0


if not customers:
    print("All customers were driven to their destinations")
    print(f"Total time: {time} minutes")
else:
    print("Not all customers were driven to their destinations")
    print(f"Customers left: {', '.join(map(str, customers))}")
