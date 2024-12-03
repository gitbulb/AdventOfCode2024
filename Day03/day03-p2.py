import re

with open("Day03/memory") as memory_file:
    memory = memory_file.read()

opcodes = re.finditer("(mul|do|don't)\(([0-9,]*)\)", memory)

result = 0
do = True
for opcode in opcodes:
    # print(opcode)
    if opcode.group(1) == "do":
        do = True
    if opcode.group(1) == "don't":
        do = False

    if do and opcode.group(1) == "mul":
        # print(opcode)
        nums = re.search("([0-9]+),([0-9]+)", opcode.group(0))
        if nums:
            # print(nums)
            result += int(nums.group(1)) * int(nums.group(2))


print("Result of adding multiplications (88802350): %d" % (result))
