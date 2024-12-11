
hmap = []

# Get steps from position pos that are within the map
def get_steps(pos):
    steps = []

    # right, down, left, up
    for step in (1,0), (0,1), (-1,0), (0,-1):

        x = pos[0]+step[0]
        y = pos[1]+step[1]
        # If within map
        if 0 <= x < len(hmap[0]) and 0 <= y < len(hmap):

            steps.append((x,y))
    return steps

def travel_trail(pos):

    tops=0
    if hmap[pos[1]][pos[0]] == 9:
        return 1

    steps = get_steps(pos)
    for step in steps:
        if hmap[step[1]][step[0]] == hmap[pos[1]][pos[0]] +1:
            tops += travel_trail(step)

    return tops



def find_zero(hmap):
    zeros = []
    for y in range(len(hmap)):
        for x in range(len(hmap[y])):
            if hmap[y][x] == 0:
                zeros.append((x,y))
    return zeros

for line in open('Day10/map'):
    map_line = []
    line = line.strip()
    for item in line:
        if item == ".":
            map_line.append(-1)
        else:
            map_line.append(int(item))

    hmap.append(map_line)
zeros = find_zero(hmap)

total_score = 0
for zero in zeros:
    score = travel_trail( zero)
    # print(score)
    total_score += travel_trail( zero)

print(f"Total trailheads ( 1034 / 81) : {total_score}")
