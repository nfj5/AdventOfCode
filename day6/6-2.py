import argparse


class LanternFish:
    def __init__(self, days, num_fish):
        self.days = int(days)
        self.num_fish = int(num_fish)

    def step(self):
        if self.days == 0:
            self.days = 6
            return True
        self.days -= 1
        return False

    def __repr__(self):
        return str(self.days) + "(x" + str(self.num_fish) + ")"


def read_file(file):
    raw_fish = {}
    with open(file, "r") as input_file:
        all_fish = input_file.readlines()[0].strip()
        for days in all_fish.split(","):
            if days not in raw_fish:
                raw_fish[days] = 1
            else:
                raw_fish[days] += 1

    lantern_fish = []
    for day in raw_fish:
        lantern_fish.append(LanternFish(day, raw_fish[day]))
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
        num_new_fish = 0

        for i in range(num_fish):
            curr_fish = fish[i]
            if curr_fish.step():
                num_new_fish += curr_fish.num_fish

        if num_new_fish:
            fish.append(LanternFish(8, num_new_fish))

    print(sum([f.num_fish for f in fish]))

# 1746710169834
