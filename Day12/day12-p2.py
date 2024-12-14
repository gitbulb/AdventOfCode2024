UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

def direction_char(dir):
    if dir == UP:
        return "^"
    if dir == RIGHT:
        return ">"
    if dir == DOWN:
        return "_"
    if dir == LEFT:
        return "<"


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

def get_fence_from_garden(garden, dir):

    x = garden[0]
    y = garden[1]

    # Fence between garden: -> garden_pos *2
    x = x*2 + 1
    y = y*2 + 1

    # "delta"-1
    return (get_next_garden((x,y), dir), dir)



def list_fences(gardens, garden):

    fences = []
    for dir in [UP, RIGHT, DOWN, LEFT]:
        # Look in each direction if fence (not same)
        n_garden = get_next_garden(garden, dir)
        if not same_garden(gardens, garden, n_garden):
            # Hit a fence in "dir" direction
            fences.append( get_fence_from_garden(garden, dir) )
    return fences


def get_all_fences_of_plot(gardens, plot):

    # List all separate fences
    fences = []
    for garden in plot:
        fences += list_fences(gardens, garden)

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


def build_fence_map(fences, max_x, max_y, gardens):

    # Expand regular map by factor 2 and "shift" 1
    # Thereby garden on odd coordinates, fences on even coordinates

    fence_map = []
    for y in range((max_y*2)+1):
        fence_map.append(["."]*((max_x*2)+1))

    for y in range(len(gardens)):
        for x in range(len(gardens[0])):

            garden = gardens[y][x]
            fx = (x*2)+1
            fy = (y*2)+1
            fence_map[fy][fx] = garden


    for fence in fences:
        # fence coordinates already corrected
        (x,y), dir = fence
        fence_map[y][x] = direction_char(dir)

    return fence_map

def get_sides(analyze):
    # Cleanup
    analyze = "".join([analyze[i] for i in range(1,len(analyze),2)])

    sides = 0
    if analyze[0] != ".":
        sides = 1
    for i in range(1,len(analyze)):
        if analyze[i] != analyze[i-1]:
            if analyze[i] != ".":
                sides += 1

    return sides




def get_fence_sides(fence_map):

    sides = 0
    # Loop over vertical sides
    for col in range(0, len(fence_map[0]),2):
        analyze = [ fence_map[p][col] for p in range(len(fence_map)) ]
        sides += get_sides(analyze)

    # Loop over horizontal sides
    for row in range(0, len(fence_map),2):
        analyze = fence_map[row]
        sides += get_sides(analyze)

    return sides





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

        fences = get_all_fences_of_plot(gardens, plot)

        fence_map = []
        fence_map = build_fence_map(fences, len(gardens[0]), len(gardens), gardens)

        sides = get_fence_sides(fence_map)

        cost = len(plot) * sides
        total_cost += cost


        print(f"Plot with plant '{gardens[y][x]}' has {len(plot)} gardens, {len(fences)} fences, {sides} sides, costs {cost}")

print(f"Total cost ( 1518548 / 1930): {total_cost}")
