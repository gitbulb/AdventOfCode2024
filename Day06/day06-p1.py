# Number upwards when rotating 90 degrees right
UP=0
RIGHT=1
DOWN=2
LEFT=3

matrix = []


# Find start position
def find_start():
    for y in range(len(matrix)):
        x = "".join(matrix[y]).find("^")
        if x > -1:
            return x,y

def within_map(x, y):
     return 0 <= x < len(matrix[0]) and 0 <= y < len(matrix)
def get_next(x, y, direction):

    if direction == UP:
        y = y - 1
    if direction == DOWN:
        y = y + 1

    if direction == RIGHT:
         x = x + 1
    if direction == LEFT:
         x = x - 1

    return x, y

def turn(direction):
    return (direction +1) % 4

def navigate_next(x, y, direction):
    # Mark current position
    matrix[y][x] = "X"
    # Look ahead
    next_x, next_y = get_next(x, y, direction)
    # while blocked, turn and look ahead
    while within_map(next_x, next_y) and  matrix[next_y][next_x] == "#":
        direction = turn(direction)
        next_x, next_y = get_next(x, y, direction)
    # return next location
    return next_x, next_y, direction


def get_positions():
    counter = 0
    for line in matrix:
        counter += "".join(line).count("X")

    return counter



# matrix = [ list(line.strip()) for line in open('Day06/map_example_p1') ]
matrix = [ list(line.strip()) for line in open('Day06/map') ]



x,y = find_start()
direction = UP
# Continue while within the map coordinates
while within_map(x,y):
    x, y, direction = navigate_next(x, y, direction)



print(f"Number of positions (5318): {get_positions()}")
