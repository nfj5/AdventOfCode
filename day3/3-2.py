def get_bits(bits, index, desired):
    result_bits = []

    for bit in bits:
        if bit[index] == desired:
            result_bits.append(bit)

    return result_bits


def get_rating(bits, oxygen):
    num_bits = len(bits[0])
    remainder = bits

    n = 0
    while n < num_bits and len(remainder) != 1:
        nth_bits = [bit[n] for bit in remainder]
        num_zeros = nth_bits.count(0)
        num_ones = nth_bits.count(1)

        if num_ones > num_zeros:
            if oxygen:
                remainder = get_bits(remainder, n, 1)
            else:
                remainder = get_bits(remainder, n, 0)
        elif num_zeros > num_ones:
            if oxygen:
                remainder = get_bits(remainder, n, 0)
            else:
                remainder = get_bits(remainder, n, 1)
        else:
            if oxygen:
                remainder = get_bits(remainder, n, 1)
            else:
                remainder = get_bits(remainder, n, 0)

        n += 1

    if len(remainder) > 1:
        raise Exception("cannot have more than one result")

    return remainder[0]


with open("input.txt", "r") as input_file:
    lines = input_file.readlines()

    raw_bits = []

    for i, line in enumerate(lines):
        raw_bits.append([int(bit) for bit in line.strip()])

    oxygen_rating = get_rating(raw_bits, True)
    scrubber_rating = get_rating(raw_bits, False)

    oxygen_rating_num = int(''.join(map(str, oxygen_rating)), 2)
    scrubber_rating_num = int(''.join(map(str, scrubber_rating)), 2)

    result = oxygen_rating_num * scrubber_rating_num
    print(result)

    # 4267809
