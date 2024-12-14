import re

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

def get_robots(robots_map, min_x, max_x, min_y, max_y):

    sum = 0
    for y in range(min_y, max_y+1):
        for x in range(min_x, max_x+1):
            sum += robots_map[y][x]
    return sum


robots = read_robots_file("Day14/robots")
num_x = 101
num_y = 103

# robots = read_robots_file("Day14/robots_example")
# num_x = 11
# num_y = 7

# Perform the steps/seconds
seconds = 100
for _ in range(seconds):
    for robot in range(len(robots)):
        robots[robot] = move(robots[robot], num_x, num_y)

# Set up robot map
robot_map = []
for y in range(num_y):
    robot_map.append( [0] * num_x )

# Show/Calculate positions
for robot in robots:
    robot_map[robot[0][1]][robot[0][0]] += 1

robot_counter = 1 # Results are multiplied, so do not start at zero...
# Quad1
min_x = 0
max_x = (num_x // 2) -1
min_y = 0
max_y = (num_y // 2) -1

robot_counter *= get_robots(robot_map, min_x, max_x, min_y, max_y)

# Quad2
min_x = (num_x // 2) +1
max_x = num_x -1
min_y = 0
max_y = (num_y // 2) -1
robot_counter *= get_robots(robot_map, min_x, max_x, min_y, max_y)

# Quad3
min_x = (num_x // 2) +1
max_x = num_x -1
min_y = (num_y // 2) +1
max_y = num_y -1
robot_counter *= get_robots(robot_map, min_x, max_x, min_y, max_y)


# Quad4
min_x = 0
max_x = (num_x // 2) -1
min_y = (num_y // 2) +1
max_y = num_y -1
robot_counter *= get_robots(robot_map, min_x, max_x, min_y, max_y)


print(f"Product of four quadrants (230686500 / 12): {robot_counter}")
