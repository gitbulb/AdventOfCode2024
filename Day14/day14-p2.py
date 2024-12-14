import re
import time
NUM_X = 101
NUM_Y = 103
X_MIDDLE = NUM_X // 2


def check_tree(robot_map, num_blocks, blocksize):

    # Check 5 neighbours
    c_n = blocksize
    blocks = 0
    for line in robot_map:

        for x in range(NUM_X- (c_n-1)):

            if line[x] == 0:
                continue

            robots = 1
            for x2 in range(c_n):
                robots *= line[x+x2]
                if robots == 0:
                    break

            if robots > 0:
                blocks += 1
                break


    return blocks >= num_blocks

def print_tree(robot_map):
    for line in robot_map:
        print(("".join([str(item) for item in line])).replace("0","."))

def generate_robot_map(robots, num_x, num_y):
    robot_map = []
    for y in range(num_y):
        robot_map.append( [0] * num_x )

# Show/Calculate positions
    for robot in robots:
        robot_map[robot[0][1]][robot[0][0]] += 1

    return robot_map

def read_robots_file(robots_file):
    robots = []
    for line in open(robots_file):

        vals = re.findall("[\-0-9]+", line.strip())

        pos = (int(vals[0]), int(vals[1]))
        speed = (int(vals[2]), int(vals[3]))
        robots.append((pos,speed))
    return robots

def move(robot, num_x, num_y):

    new_robot = ( (robot[0][0] + robot[1][0] + num_x) % num_x ,(robot[0][1] + robot[1][1] + num_y) % num_y)
    return ( new_robot, robot[1] )



robots = read_robots_file("Day14/robots")


# robots = read_robots_file("Day14/robots_example")
# num_x = 11
# num_y = 7

time_start = time.time()
# Perform the steps/seconds
seconds = 10000
found_round = 0
for n in range(seconds):
    for robot in range(len(robots)):
        robots[robot] = move(robots[robot], NUM_X, NUM_Y)

    # # # Do not check first 5000
    if n < 7000:
        if n % 100 == 0:
            print(f"Round: {n+1}")
        continue
# Set up robot map

    robot_map = generate_robot_map(robots, NUM_X, NUM_Y)

    if n % 10 == 0:
        print(f"Round: {n+1}")
        # print_tree(robot_map)

    # if n in [7669,7670,7671]:
    #     print(f"Round: {n}")
    #     print_tree(robot_map)

    if check_tree(robot_map, num_blocks=4, blocksize=4):
        print(f"Round: {n+1}")
        print_tree(robot_map)
        found_round = n+1
        break

time_stop = time.time()
print(f"Duration: {time_stop-time_start}")
print(f"Found the tree in round (7672): {found_round}")
