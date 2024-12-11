
stones_input = "41078 18 7 0 4785508 535256 8154 447" # puzzle input
# stones_input = "125 17" # example input

blinks = 25

stones = stones_input.split()


for blink in range(blinks):
    pos = 0
    while pos < len(stones):

        stone = stones[pos]
        if stone == "0":
            stones[pos] = "1"

        elif len(stone) % 2 == 0:
            # Do str(int()) to remove leading zeroes
            x_stone1 = stone[:int(len(stone)/2)]
            x_stone2 = str(int(stone[int(len(stone)/2)*-1:]))

            stones[pos] = x_stone1
            pos += 1
            stones.insert(pos, x_stone2)

        else:
            stones[pos] = str(int(stone)*2024)


        pos += 1

print(f"Number of stones ( 217443 / 55312): {len(stones)}")
