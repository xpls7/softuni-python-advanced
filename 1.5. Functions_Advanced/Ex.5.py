def even_odd(nums, command):
    if command == "Even":
        even_sum = sum(filter(lambda x: x % 2 == 0, nums))
        return even_sum * len(nums)
    elif command == "Odd":
        odd_sum = sum(filter(lambda x: x % 2 == 1, nums))
        return odd_sum * len(nums)


command = input()
numbers = list(map(lambda x: int(x), input().split()))
print(even_odd(numbers, command))
