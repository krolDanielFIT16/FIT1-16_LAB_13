from p2_module import *

lst: list[ENTERPRISE] = [
    ENTERPRISE("A", 10000, "2010", "OA"),
    ENTERPRISE("B", 500, "2000", "OA"),
    ENTERPRISE("C", 100, "2020", "OB"),
    ENTERPRISE("D", 9000, "1990", "OC"),
    ENTERPRISE("C", 200000, "1995", "OC"),
]


moreThanMil = []
multiOwners = {}

for i in lst:
    if i.GetFinance() > 1000:
        moreThanMil.append(str(i))
    if not i.GetOwner() in multiOwners:
        multiOwners[i.GetOwner()] = 0
    multiOwners[i.GetOwner()] += 1

for i in moreThanMil:
    print(i)
print()
for k in multiOwners.keys():
    if multiOwners[k] > 1:
        print(k, end=" ")
