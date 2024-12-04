XMAS_LEN = 4
xmas_blob = []

# Room functions check is XMAS will fit in that direction
def room_up(line):
    return line >= XMAS_LEN -1
def room_down(line):
    return line <= len(xmas_blob) - XMAS_LEN
def room_forward(line, pos):
    return pos < len(xmas_blob[line]) - XMAS_LEN
def room_reverse(pos):
    return pos >= XMAS_LEN-1

def check_xmas_quadrant_1(line, pos):
    # Right, Upper
    if room_forward(line, pos) and room_up(line):
        return xmas_blob[line][pos] == "X" and xmas_blob[line-1][pos+1] == "M" and xmas_blob[line-2][pos+2] == "A" and xmas_blob[line-3][pos+3] == "S"
    return False

def check_xmas_quadrant_2(line, pos):
    # Left, Upper
    if room_reverse(pos) and room_up(line):
        return xmas_blob[line][pos] == "X" and xmas_blob[line-1][pos-1] == "M" and xmas_blob[line-2][pos-2] == "A" and xmas_blob[line-3][pos-3] == "S"
    return False

def check_xmas_quadrant_3(line, pos):
    # Left, Lower
    if room_reverse(pos) and room_down(line):
        return xmas_blob[line][pos] == "X" and xmas_blob[line+1][pos-1] == "M" and xmas_blob[line+2][pos-2] == "A" and xmas_blob[line+3][pos-3] == "S"
    return False


def check_xmas_quadrant_4(line, pos):
    # Right, Lower
    if room_forward(line, pos) and room_down(line):
        return xmas_blob[line][pos] == "X" and xmas_blob[line+1][pos+1] == "M" and xmas_blob[line+2][pos+2] == "A" and xmas_blob[line+3][pos+3] == "S"
    return False


def check_xmas_down(line, pos):
    if room_down(line):
        return xmas_blob[line][pos] == "X" and xmas_blob[line+1][pos] == "M" and xmas_blob[line+2][pos] == "A" and xmas_blob[line+3][pos] == "S"
    return False

def check_xmas_up(line, pos):
    if room_up(line):
        return xmas_blob[line][pos] == "X" and xmas_blob[line-1][pos] == "M" and xmas_blob[line-2][pos] == "A" and xmas_blob[line-3][pos] == "S"
    return False


def check_xmas_forward(line, pos):
    if room_forward(line, pos):
        return xmas_blob[line][pos:pos+XMAS_LEN] == "XMAS"
    return False


def check_xmas_reverse(line, pos):
    if room_reverse(pos):
        return xmas_blob[line][pos-(XMAS_LEN-1):pos+1] == "SAMX"
    return False


def check_xmas(line, pos):
    counter = 0
    if xmas_blob[line][pos] == "X":
        counter += 1 if check_xmas_forward(line, pos) else 0
        counter += 1 if check_xmas_reverse(line,pos) else 0
        counter += 1 if check_xmas_up(line, pos) else 0
        counter += 1 if check_xmas_down(line, pos) else 0
        counter += 1 if check_xmas_quadrant_1(line, pos) else 0
        counter += 1 if check_xmas_quadrant_2(line, pos) else 0
        counter += 1 if check_xmas_quadrant_3(line, pos) else 0
        counter += 1 if check_xmas_quadrant_4(line, pos) else 0
    return counter

with open("Day04/xmas") as xmas_file:
    xmas_blob = xmas_file.readlines()

counter=0
for line in range(0, len(xmas_blob)):
    for pos in range(0, len(xmas_blob[line])):
        # print(xmas_blob[line][pos], end="")
        counter += check_xmas(line, pos)
            # print(xmas_blob[line])
    # print("")

print("Counted XMAS %d times (2646)" % (counter))
