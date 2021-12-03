gamma = []

with open("input.txt", "r") as input_file:
    lines = input_file.readlines()

    bits = []

    for i, line in enumerate(lines):
        bits.append([int(bit) for bit in line.strip()])

    num_bits = len(bits[0])

    for n in range(num_bits):
        nth_bits = [bit[n] for bit in bits]
        num_ones = nth_bits.count(1)
        num_zeros = nth_bits.count(0)

        if num_ones > num_zeros:
            gamma.append(1)
        else:
            gamma.append(0)

    alpha = [0 if bit == 1 else 1 for bit in gamma]

    gamma_as_num = int(''.join(map(str, gamma)), 2)
    alpha_as_num = int(''.join(map(str, alpha)), 2)

    result = gamma_as_num * alpha_as_num
    print(result)

    # 3969000
