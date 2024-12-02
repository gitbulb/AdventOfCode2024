
def occurences(aList, searchEntry):
    counter = 0
    for item in aList:
        if item == searchEntry:
            counter += 1
    return counter

list1 = []
list2 = []
with open("Day01/list") as file:
    for line in file:
        l =  line.split()
        list1.append(int(l[0]))
        list2.append(int(l[1]))

res = 0

for p1 in list1:
    occs = occurences(list2, p1)
    res += p1 * occs
    # print("%d  * %d =  %d" % (occs, p1, p1 * occs))

print("Total similarity score: %d" % (res))
