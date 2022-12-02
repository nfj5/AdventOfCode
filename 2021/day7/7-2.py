import sys
from tqdm import tqdm


def total_fuel(crabs, end):
    return sum(get_fuel(crab, end) for crab in crabs)


def get_fuel(start, end):
    return sum([i for i in range(abs(end - start) + 1)])


def read_file(file_name):
    positions = []
    with open(file_name, "r") as input_file:
        raw_pos = input_file.readlines()[0].strip()
        for pos in raw_pos.split(","):
            positions.append(int(pos))
    return positions


if __name__ == "__main__":
    crab_pos = read_file("input.txt")
    max_crab = max(crab_pos)
    min_crab = min(crab_pos)

    min_fuel = (sys.maxsize, -1)
    for i in tqdm(range(min_crab, max_crab + 1)):
        fuel_required = total_fuel(crab_pos, i)
        min_fuel = (min(min_fuel[0], fuel_required), i)

    print(min_fuel)
