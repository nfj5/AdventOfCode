def puzzle_to_int_list(input_puzzle):
    result_puzzle = []
    for line in input_puzzle:
        result_puzzle.append([])
        split_up = line.split(" ")
        for part in split_up:
            if part:
                result_puzzle[len(result_puzzle) - 1].append(int(part))
    return result_puzzle


def play_option(option, input_puzzle):
    for i, line in enumerate(input_puzzle):
        for j, board_option in enumerate(line):
            if board_option == option:
                input_puzzle[i][j] = 0
    return input_puzzle


def check_win(input_puzzle):
    for row in range(len(input_puzzle)):
        # rows
        if input_puzzle[row].count(0) == 5:
            return True
        # cols
        if [input_puzzle[col][row] for col in range(len(input_puzzle))].count(0) == 5:
            return True

    return False


def get_remaining_board_sum(input_puzzle):
    result = 0
    for i in range(len(input_puzzle)):
        for j in range(len(input_puzzle)):
            result += input_puzzle[i][j]
    return result


puzzles = []

with open("input.txt", "r") as input_file:
    lines = [line.strip() for line in input_file.readlines()]

    options = [int(option) for option in lines[0].split(",")]

    current_line = 2
    while current_line < len(lines):
        current_puzzle = lines[current_line:current_line+5]
        puzzle = puzzle_to_int_list(current_puzzle)
        puzzles.append(puzzle)
        current_line += 6

for option in options:
    for puzzle in puzzles:
        puzzle = play_option(option, puzzle)

        if check_win(puzzle):
            puzzle_sum = get_remaining_board_sum(puzzle)
            puzzle_result = puzzle_sum * option
            print(puzzle_result)
            exit()

print("No wins!")