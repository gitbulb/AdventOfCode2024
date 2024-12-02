
list1 = []
list2 = []
with open("Day01/list") as file:
    for line in file:
        l =  line.split()
        list1.append(int(l[0]))
        list2.append(int(l[1]))

list1.sort()
list2.sort()

res = 0

for p1, p2 in zip(list1, list2):
    res += abs(p2 - p1)
    # print("%d  - %d =  %d" % (p2, p1, res))

print("Total distance between lists: %d" % (res))

