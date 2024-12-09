# diskmap = [ list(line.strip()) for line in open('Day09/diskmap_example1') ]




def get_disk_layout(diskmap):
    file_info  = [None] * int(len(diskmap)/2)
    disk = []
    id = 0
    for pos in range(0,len(diskmap),2):
        # Store "size" of file
        id_len = diskmap[pos]
        spaces = diskmap[pos+1]

        file_info[id] = int(id_len)

        for i in range(int(id_len)):
            disk.append(str(id))
        for i in range(int(spaces)):
            disk.append(".")

        id += 1

    return disk, file_info

def optimize_layout(disk):

    begin = 0
    end = len(disk)-1

    while begin < end:
        while disk[begin] != ".":
            begin += 1
        if begin >= end:
            break
        disk[begin] = disk[end]
        disk[end] = "."
        while disk[end] == ".":
            end -= 1


def get_length(a_string, a_char, direction, pos ):

    the_length = 0
    while a_char == a_string[pos]:
        the_length += 1
        pos += direction

    return the_length


def optimize_layout_p2(disk, file_info):

    # scan from right to left:
    i = len(disk)-1

    # A "shadow" disk to easily search for empty spaces "#"
    # ID's are not relevant when searching for spaces, so reduce each ID to a single (first) character
    disk_string = "".join([x[0] for x in disk])
    while i >= 0:

        if i % 1000 == 0:
            print(f"Counter: {i}")

        if disk[i] != ".":
            file_len = file_info[int(disk[i])]
            file_space = "".join(["."] * file_len)

            pos = (disk_string.find(file_space))
            if pos > 0 and pos < i:
                for x in range(file_len):
                    disk[pos+x] = disk[i]
                    disk_string = disk_string[:pos+x] + "0" + disk_string[pos+x + 1:]
                for x in range(file_len):
                    disk[i-x] = "."
                    disk_string = disk_string[:i-x] + "." + disk_string[i-x + 1:]


            i -= file_len

        else:
            i -= 1


def calc_checksum(disk):

    checksum = 0
    for i in range(len(disk)):
        if disk[i] != ".":
            checksum += i * int(disk[i])

    return checksum

# disk_map = open('Day09/diskmap_example1').read().strip()
disk_map = open('Day09/diskmap').read().strip()
disk_map += "0"

disk, file_info = get_disk_layout(disk_map)

optimize_layout_p2(disk, file_info)
# print("".join(disk))

checksum = calc_checksum(disk)


print(f"Checksum is ( 6349492251099 / 2858): {checksum}")
