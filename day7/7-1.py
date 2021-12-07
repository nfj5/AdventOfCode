import sys


def total_fuel(crabs, end):
    return sum(get_fuel(crab, end) for crab in crabs)


def get_fuel(start, end):
    return abs(end - start)


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

    min_fuel = sys.maxsize
    for i in range(min_crab, max_crab + 1):
        fuel_required = total_fuel(crab_pos, i)
        min_fuel = min(min_fuel, fuel_required)
    print(min_fuel)
