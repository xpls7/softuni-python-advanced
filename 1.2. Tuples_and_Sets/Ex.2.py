n_m = input().split()

n = int(n_m[0])
m = int(n_m[1])

n_set = set()
m_set = set()

for row in range(n+m):
    num = input()

    if row < n:
        n_set.add(num)
    else:
        m_set.add(num)

modified_set = n_set.intersection(m_set)
for el in modified_set:
    print(el)





