import itertools


def find_antennas(nodes, freq):
    antennas = []
    for y in range(len(nodes)):
        for x in range(len(nodes[0])):
            if nodes[y][x] == freq:
                antennas.append((x,y))
    return antennas

def calc_antinodes(node1, node2, max_x, max_y):

    antinodes = set()

    # Any set of pairs are a set of anti nodes!!!!!!
    antinodes.add(node1)
    antinodes.add(node2)
    # Get diff node 2->1, apply node2 -> antinode
    dx = node2[0] - node1[0]
    dy = node2[1] - node1[1]

    # Look forward node2[0]+dx, node2[1]+dy
    loop_counter = 1
    ax, ay = node2[0]+(dx*loop_counter), node2[1]+(dy*loop_counter)
    while 0 <= ax <= max_x and 0 <= ay <= max_y:
        antinodes.add((ax, ay))

        loop_counter += 1
        ax, ay = node2[0]+(dx*loop_counter), node2[1]+(dy*loop_counter)


    # Look back node1[0]-dx, node1[1]-dy
    loop_counter = 1
    ax, ay = node1[0]-(dx*loop_counter), node1[1]-(dy*loop_counter)
    while 0 <= ax <= max_x and 0 <= ay <= max_y:
        antinodes.add((ax, ay))

        loop_counter += 1
        ax, ay = node1[0]-(dx*loop_counter), node1[1]-(dy*loop_counter)

    # return (node1[0]-dx, node1[1]-dy),(node2[0]+dx, node2[1]+dy)
    return antinodes


def find_antinodes(antinodes, antennas):

    rows = len(antinodes)
    cols = len(antinodes[0])
    combinations = list(itertools.combinations(antennas, r=2))

    for combination in combinations:
        for anti in calc_antinodes(combination[0], combination[1],cols-1, rows-1):
            if 0 <= anti[0] < cols and 0 <= anti[1] < rows:
                antinodes[anti[1]][anti[0]] = "#"



def count_antinodes(antinodes):
    counter = 0
    for line in antinodes:
        counter += "".join(line).count("#")

    return counter

# Generate 0-9, a-z, A-Z
frequencies = \
    [chr(ord("0")+x) for x in range(10)] + \
    [chr(ord("a")+x) for x in range(26)] + \
    [chr(ord("A")+x) for x in range(26)]

# nodes = [ list(line.strip()) for line in open('Day08/map_example') ]
nodes = [ list(line.strip()) for line in open('Day08/map') ]

antinodes = []
for y in range(len(nodes)):
    antinodes.append(["."]*len(nodes[y]))

for freq in frequencies:
    antennas = find_antennas(nodes, freq)
    if len(antennas) > 0:
        find_antinodes(antinodes, antennas)

print(f"Number of antinodes (1285 / 34): {count_antinodes(antinodes)}")
