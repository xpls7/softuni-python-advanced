number = int(input())

f_list = []

for _ in range(number):
    data = input().split()
    action = int(data[0])

    if action == 1:
        new_num = int(data[1])
        f_list.append(new_num)
    elif action == 2:
        if f_list:
            f_list.pop()
    elif action == 3:
        if f_list:
            print(max(f_list))
    elif action == 4:
        if f_list:
            print(min(f_list))

last_list = []
for _ in range(len(f_list)):
    last_list.append(f_list.pop())
print(", ".join(map(str, last_list)))
