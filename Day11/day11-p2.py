import functools
import time


@functools.lru_cache(maxsize=None)
def blink_stone(stone):

    if stone == "0":
        return "1", None

    if len(stone) % 2 == 0:
        # Do str(int()) to remove leading zeroes
        split = int(len(stone)/2)
        x_stone1 = stone[:split]
        x_stone2 = stone[split*-1:]
        if x_stone2[0] == "0":
            x_stone2 = str(int(x_stone2))

        return x_stone1, x_stone2

    return str(int(stone)*2024), None


@functools.lru_cache(maxsize=None)
def count_stones(stone, blinks) -> int:

    counter = 0
    if stone is None:
        return 0

    # Only count leaves
    if blinks == 0:
        return 1


    stone1, stone2 = blink_stone(stone)

    counter += count_stones(stone1, blinks-1)
    counter += count_stones(stone2, blinks-1)

    return counter



stones_input = "41078 18 7 0 4785508 535256 8154 447" # puzzle input
# stones_input = "125 17" # example input
blinks = 75
# blinks = 25
stones = stones_input.split()


start_time = time.time()


stone_counter = 1
counter = 0
for stone  in stones:
    counter += count_stones(stone, blinks)

    print(f"Turned stone {stone_counter} of {len(stones)}")
    stone_counter += 1

stop_time = time.time()

print(f"Number of stones ( p2 257246536026785 / p1 217443 / ex 55312): {counter}, time: {stop_time-start_time}")
