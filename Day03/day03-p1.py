import re

with open("Day03/memory") as memory_file:
    memory = memory_file.read()

muls = re.finditer('mul\(([0-9]+),([0-9]+)\)', memory)

result=0
for mul in muls:
    # print(mul)
    result += int(mul.group(1)) * int(mul.group(2))

print("Result of adding multiplications (174336360): %d" % (result))
