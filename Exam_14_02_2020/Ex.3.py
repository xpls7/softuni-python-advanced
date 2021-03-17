def stock_availability(flavours, command, *args):
    from collections import deque
    flavours = deque(flavours)

    if command == "delivery":
        for a in args:
            flavours.append(a)

    if command == "sell":
        if not args:
            flavours.popleft()
        elif isinstance(args[0], int):
            for i in range(args[0]):
                flavours.popleft()
        elif isinstance(args[0], str):
            flavours = list(flavours)
            items = list(args)
            for item in items:
                for el in range(len(flavours)):
                    if item in flavours:
                        flavours.remove(item)
                    else:
                        break

    return list(flavours)


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
