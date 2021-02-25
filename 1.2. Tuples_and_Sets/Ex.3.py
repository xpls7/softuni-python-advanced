n = int(input())

chemical_compounds = set()

for i in range(n):

    elements = input().split()
    for el in elements:
        chemical_compounds.add(el)

for a in chemical_compounds:
    print(a)
