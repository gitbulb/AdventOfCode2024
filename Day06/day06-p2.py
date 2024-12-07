import copy
import time

# Number upwards when rotating 90 degrees right
UP=0
RIGHT=1
DOWN=2
LEFT=3


# Find start position
def find_start(matrix):
    for y in range(len(matrix)):
        x = "".join(matrix[y]).find("^")
        if x > -1:
            return x,y

def within_map(matrix, x, y):
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

def direction_icon(direction):
    icons = "^>ˇ<"

    return icons[direction]

def is_block(aChar):
    return aChar == "#" or aChar == "O"


def step_forward(matrix, x, y, direction, blocks):

    # Possible next step
    next_x, next_y = get_next(x, y, direction)

    if within_map(matrix, next_x, next_y):
        # Check for possible block
        while is_block(matrix[next_y][next_x]):
            # We hit a block
            blocks.append( [next_x, next_y] )

            # Block make us turn 90 degrees
            direction = turn(direction)

            # Re-get next step with new direction
            next_x, next_y = get_next(x, y, direction)

    # On or Off-map return that position
    return next_x, next_y, direction, blocks


def visited(matrix_main, x, y):
    return matrix_main[y][x] == "X"

def test_loop_block(matrix, matrix_main, start_x, start_y, current_x, current_y, direction):

    # Show start position and direction
    matrix[start_y][start_x] = direction_icon(UP)

    # Get next position
    next_x, next_y = get_next(current_x, current_y, direction)
    if within_map(matrix, next_x, next_y):
        # Check for possible block
        while is_block(matrix[next_y][next_x]):
            # Block make us turn 90 degrees
            direction = turn(direction)

            # Re-get next step with new direction
            next_x, next_y = get_next(current_x, current_y, direction)



    # !! Also do not test position/blocks that have already been tested; avoid counting the same block multiple times, and may speed up
    # if next on map and next is not already a block
    if within_map(matrix, next_x,next_y) and not is_block(matrix[next_y][next_x]) and not visited(matrix_main, next_x,next_y):
        # Place test block on next
        matrix[next_y][next_x] = "O"


        x,y = start_x,start_y
        direction = UP
        blocks = []

        is_loop = None
        # Run trace from start
        while True:
            x, y, direction, blocks  = step_forward(matrix, x, y, direction, blocks)

            if within_map(matrix, x,y):
                if matrix[y][x] == direction_icon(direction):
                    # for line in matrix: print("".join(line))
                    # print("")
                    is_loop = True
                    break
                else:
                    matrix[y][x] = direction_icon(direction)

            if not within_map(matrix, x,y):
                is_loop =False
                break



        # Remove placed block
        matrix[next_y][next_x] = "."
        if is_loop is None:
            print("Loop not either True or False...???")
        return is_loop
    return False



start = time.time()
# matrix_main = [ list(line.strip()) for line in open('Day06/map_example_p1') ]
matrix_main = [ list(line.strip()) for line in open('Day06/map') ]


start_x,start_y = find_start(matrix_main)
x,y = start_x,start_y
direction = UP
possible_block_counter = 0
position_counter = 1

blocks = []
positions = []
matrix_main[y][x] = "X"
while within_map(matrix_main, x,y):

    # Test the loop before making the "next" step
    matrix_test = copy.deepcopy(matrix_main)
    if test_loop_block( matrix_test, matrix_main, start_x, start_y, x, y, direction):
        possible_block_counter += 1

    x, y, direction, blocks  = step_forward(matrix_main, x, y, direction, blocks)


    if within_map(matrix_main, x, y):
        matrix_main[y][x] = "X"
        position_counter += 1

    if position_counter % 10 == 0:
        print(f"Possition {position_counter} of 5973/41, blocks found: {possible_block_counter} ")

def get_positions():
    counter = 0
    for line in matrix_main:
        counter += "".join(line).count("X")

    return counter



print(f"Number of positions (5318/41)     : {get_positions()} - Steps (5973/45): {position_counter}")
print(f"Number of possible blocks (1831/6): {possible_block_counter}")

end = time.time()
print(end - start)
