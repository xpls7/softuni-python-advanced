text = list(map(int, input().split()))
new_list = []
for _ in range(len(text)):
    new_list.append(str(text.pop()))
print(" ".join(new_list))
