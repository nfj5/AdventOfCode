with open("input.txt", "r") as input_file:
    lines = input_file.readlines()
    num_increases = 0

    for i in range(len(lines)-3):
        a = sum(int(x) for x in lines[i:i+3])
        b = sum(int(x) for x in lines[i+1:i+4])

        if b > a:
            num_increases += 1

    print(num_increases)

# 1761
