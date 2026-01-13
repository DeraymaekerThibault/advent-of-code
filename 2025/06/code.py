import sys


def parse_input(input_file):
    with open(input_file, "r") as f:
        lines = [line.rstrip("\n") for line in f]

    if not lines:
        return [], []

    # Pad lines to max length
    max_len = max(len(line) for line in lines)
    padded_lines = [line.ljust(max_len) for line in lines]

    # Identify separator columns (all spaces)
    is_empty_col = []
    for col_idx in range(max_len):
        is_empty = True
        for line in padded_lines:
            if line[col_idx] != " ":
                is_empty = False
                break
        is_empty_col.append(is_empty)

    # Group columns into blocks
    blocks = []
    current_block_indices = []

    for col_idx, is_empty in enumerate(is_empty_col):
        if not is_empty:
            current_block_indices.append(col_idx)
        elif current_block_indices:
            blocks.append(current_block_indices)
            current_block_indices = []

    if current_block_indices:
        blocks.append(current_block_indices)

    return padded_lines, blocks


def get_operator(padded_lines, block_indices):
    op_line_chars = [padded_lines[-1][i] for i in block_indices]
    op_str = "".join(op_line_chars).strip()
    return op_str


def solve_part1(padded_lines, blocks):
    grand_total = 0
    for block_indices in blocks:
        operator = get_operator(padded_lines, block_indices)
        numbers = []
        for line_idx in range(len(padded_lines) - 1):
            line_chars = [padded_lines[line_idx][i] for i in block_indices]
            num_str = "".join(line_chars).strip()
            if num_str:
                numbers.append(int(num_str))

        if operator == "*":
            res = 1
            for n in numbers:
                res *= n
            grand_total += res
        elif operator == "+":
            res = 0
            for n in numbers:
                res += n
            grand_total += res

    return grand_total


def solve_part2(padded_lines, blocks):
    grand_total = 0
    for block_indices in blocks:
        operator = get_operator(padded_lines, block_indices)
        numbers = []

        # Iterate columns right-to-left
        for col_idx in reversed(block_indices):
            # Extract digits from rows 0 to N-2
            col_chars = []
            for line_idx in range(len(padded_lines) - 1):
                char = padded_lines[line_idx][col_idx]
                col_chars.append(char)

            num_str = "".join(col_chars).strip()
            if num_str:
                numbers.append(int(num_str))

        if operator == "*":
            res = 1
            for n in numbers:
                res *= n
            grand_total += res
        elif operator == "+":
            res = 0
            for n in numbers:
                res += n
            grand_total += res

    return grand_total


def solve(input_file):
    padded_lines, blocks = parse_input(input_file)
    p1 = solve_part1(padded_lines, blocks)
    p2 = solve_part2(padded_lines, blocks)
    print(p1)
    print(p2)
    return p1, p2


if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_path = sys.argv[1]
    else:
        input_path = "input.txt"

    solve(input_path)
