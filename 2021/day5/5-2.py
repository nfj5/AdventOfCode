def get_map(size):
    return [[0] * size for i in range(size)]


def get_score(base_map, intersections):
    score = 0

    for y, row in enumerate(base_map):
        for x, val in enumerate(row):
            if val >= intersections:
                score += 1

    return score


def draw_map(to_draw):
    for y, row in enumerate(to_draw):
        for x, val in enumerate(row):
            if val == 0:
                print(".", end=" ")
            else:
                print(val, end=" ")
        print()


def place_path(base_map, path):
    x1, y1 = path[0]
    x2, y2 = path[1]

    if x1 == x2:
        if y2 < y1:
            y1, y2 = y2, y1
        for y in range(y1, y2 + 1):
            base_map[y][x1] += 1
    elif y1 == y2:
        if x2 < x1:
            x1, x2 = x2, x1
        for x in range(x1, x2 + 1):
            base_map[y1][x] += 1
    else:
        x_increment = 1 if x1 < x2 else -1
        y_increment = 1 if y1 < y2 else -1

        for i in range(abs(x1 - x2) + 1):
            base_map[y1 + i * y_increment][x1 + i * x_increment] += 1

    return base_map


def load_file(file_path):
    largest_coord = 0

    with open(file_path, "r") as input_file:
        lines = input_file.readlines()
        paths = []

        curr_path = 0
        for line in lines:
            paths.append([])
            split = [part.strip() for part in line.split(" ") if part != "->"]

            for i, part in enumerate(split):
                x_and_y = [int(coord) for coord in part.split(",")]
                largest_coord = max(largest_coord, max(x_and_y))
                paths[curr_path].append((x_and_y[0], x_and_y[1]))

            curr_path += 1

    return get_map(largest_coord + 1), paths


board, paths = load_file("input.txt")
for path in paths:
    board = place_path(board, path)

print(get_score(board, 2))

# 20373
