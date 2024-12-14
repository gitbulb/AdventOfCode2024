
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3


def on_map(gardens, pos):
    return 0 <= pos[0] < len(gardens[0]) and 0 <= pos[1] < len(gardens)

def get_next_garden(pos, dir):
    if dir == UP:
        x = pos[0]
        y = pos[1]-1

    if dir == RIGHT:
        x = pos[0]+1
        y = pos[1]

    if dir == DOWN:
        x = pos[0]
        y = pos[1]+1

    if dir == LEFT:
        x = pos[0]-1
        y = pos[1]

    return (x,y)

def same_garden(gardens, garden, next_garden):
    # Test if same, but also on map!
    return on_map(gardens, next_garden) and gardens[garden[1]][garden[0]] == gardens[next_garden[1]][next_garden[0]]

def get_fences(gardens, garden):

    fences = 0
    for dir in [UP, RIGHT, DOWN, LEFT]:
        n_garden = get_next_garden(garden, dir)
        if not same_garden(gardens, garden, n_garden):
            fences += 1

    return fences

def get_all_fence(gardens, plot):

    fences = 0
    for garden in plot:
        fences += get_fences(gardens, garden)

    return fences

def get_neigbours_pos(gardens, garden):

    neigbours = []
    for dir in [UP, RIGHT, DOWN, LEFT]:
        n_garden = get_next_garden(garden, dir)
        if on_map(gardens, n_garden):
            neigbours.append(n_garden)

    return neigbours

def get_same_neigbours(gardens, garden):

    neigbours = []
    for neigb in get_neigbours_pos(gardens, garden):
        if gardens[garden[1]][garden[0]] == gardens[neigb[1]][neigb[0]]:
            neigbours.append(neigb)

    return neigbours



def discover_plot(gardens,garden):

    plot = []
    plot.append(garden)

    plot_len = len(plot)
    repeat = True
    while repeat:
        for grdn in range(plot_len):
            # Add each neigbour
            for neigb in get_same_neigbours(gardens, plot[grdn]):
                if not neigb in plot:
                    plot.append(neigb)

        if plot_len != len(plot):
            plot_len = len(plot)
        else:
            repeat = False

    return plot




gardens = [list(line.strip()) for line in open('Day12/map')]

visited_gardens = set()
total_cost = 0
for x in range(len(gardens[0])):
    for y in range(len(gardens)):

        if (x,y) in visited_gardens:
            continue
        # Test each point, unless in "visited" set
        plot = discover_plot(gardens,(x,y))

        for p in plot:
            visited_gardens.add(p)

        fences = get_all_fence(gardens, plot)
        cost = len(plot) * fences
        total_cost += cost
        print(f"Plot with plant '{gardens[y][x]}' has {len(plot)} gardens and {fences} fences, costs {cost}")

print(f"Total cost ( 1518548 / 1930): {total_cost}")
