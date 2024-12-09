# diskmap = [ list(line.strip()) for line in open('Day09/diskmap_example1') ]




def get_disk_layout(diskmap):
    disk = []
    id = 0
    for pos in range(0,len(diskmap),2):
        id_len = diskmap[pos]
        spaces = diskmap[pos+1]

        for i in range(int(id_len)):
            disk.append(str(id))
        for i in range(int(spaces)):
            disk.append(".")

        id += 1

    return disk

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

def calc_checksum(disk):

    checksum = 0
    for i in range(len(disk)):
        if disk[i] != ".":
            checksum += i * int(disk[i])

    return checksum

# disk_map = open('Day09/diskmap_example1').read().strip()
disk_map = open('Day09/diskmap').read().strip()
disk_map += "0"

disk = get_disk_layout(disk_map)
# print("".join(disk))

optimize_layout(disk)
checksum = calc_checksum(disk)


print(f"Checksum is ( 6334655979668 / 1928): {checksum}")
