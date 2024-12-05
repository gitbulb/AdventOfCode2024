
def check_rule(update,rule):

    try:
        # Check if both pages from rule are in update
        pos1 = update.index(rule[0])
        pos2 = update.index(rule[1])
    except ValueError:
        # One missing, just fake a correct order
        pos1 = 1
        pos2 = 2

    return pos1 < pos2




def check_update_ordering(update, rules):
    for rule in rules:
        if check_rule(update,rule) == False:
            return False
    return True


def correct_update_ordering(update, rules):
    #  Bubble sort
    for n in range(len(update) -1, 0, -1):

        for i in range(n):
            if not check_update_ordering([update[i], update[i+1]], rules):
                update[i], update[i+1] =  update[i+1], update[i]

        if check_update_ordering(update, rules):
            break


rules = []
updates = []
with open("Day05/pages") as pages_file:

    rule_section = True
    for line in pages_file:
        line = line.strip()
        if line == "":
            rule_section = False
            continue

        if rule_section:
            rules.append(line.split("|"))
        else:
            updates.append(line.split(","))


counter = 0

for update in updates:
    if not check_update_ordering(update, rules):
        # Found faulty rule, build up a new correct rule
        correct_update_ordering(update, rules)
        counter += int(update[int((len(update)-1)/2)]) # value of middle item

print("Result of adding pages (5285): %d" % (counter))
