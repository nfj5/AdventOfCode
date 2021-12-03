with open("input.txt", "r") as input_file:
    lines = input_file.readlines()
    num_increases = 0

    for i in range(len(lines)-1):
        current_depth = int(lines[i])
        next_depth = int(lines[i+1])

        if next_depth > current_depth:
            num_increases += 1

    print(num_increases)

# 1709
