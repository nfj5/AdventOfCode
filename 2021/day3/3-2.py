def get_bits(bits, index, desired):
    result_bits = []

    for bit in bits:
        if bit[index] == desired:
            result_bits.append(bit)

    return result_bits


def get_rating(bits, take_most_common):
    num_bits = len(bits[0])
    remainder = bits

    n = 0
    while n < num_bits and len(remainder) != 1:
        nth_bits = [bit[n] for bit in remainder]

        num_ones = nth_bits.count(1)
        half = len(nth_bits) / 2

        if num_ones > half or num_ones == half:
            remainder = get_bits(remainder, n, 1 if take_most_common else 0)
        elif num_ones < half:
            remainder = get_bits(remainder, n, 0 if take_most_common else 1)

        n += 1

    # just in case
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
