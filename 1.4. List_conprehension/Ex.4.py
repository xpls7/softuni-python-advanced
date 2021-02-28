numbers = [int(el) for el in input().split(', ')]

positive = []
negative = []
even = []
odd = []

for num in numbers:
    if num >= 0:
        positive.append(num)
    else:
        negative.append(num)

for n in numbers:
    if n % 2 == 0:
        even.append(n)
    else:
        odd.append(n)

print(f"Positive: {', '.join(map(str, positive))}")
print(f"Negative: {', '.join(map(str, negative))}")
print(f"Even: {', '.join(map(str, even))}")
print(f"Odd: {', '.join(map(str, odd))}")
