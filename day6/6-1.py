import argparse


class LanternFish:
    def __init__(self, days):
        self.days = int(days)

    def step(self):
        if self.days == 0:
            self.days = 6
            return True
        self.days -= 1
        return False

    def __repr__(self):
        return str(self.days)


def read_file(file):
    lantern_fish = []
    with open(file, "r") as input_file:
        all_fish = input_file.readlines()[0].strip()
        for days in all_fish.split(","):
            lantern_fish.append(LanternFish(days))
    return lantern_fish


if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("--file", help="The file to use as input")
    arg_parser.add_argument("--days", help="The number of days to run the simulation on")
    args = arg_parser.parse_args()

    if not args.file or not args.days:
        arg_parser.print_help()
        exit()

    fish = read_file(args.file)
    num_days = int(args.days)

    for day in range(num_days):
        num_fish = len(fish)
        for i in range(num_fish):
            curr_fish = fish[i]
            if curr_fish.step():
                fish.append(LanternFish(8))

    print(len(fish))

# 390011
