totals = []
curr_total = 0

with open('input.txt', 'r', encoding='utf-8') as input_file:
    lines = input_file.readlines()

    for line in lines:
        stripped = line.strip()

        if stripped == '':
            totals.append(curr_total)
            curr_total = 0
            continue

        curr_total += int(stripped)

sorted_cals = sorted(totals, reverse=True)

top_three_total = 0
for i in range(0,3):
    top_three_total += sorted_cals[i]

print(top_three_total)