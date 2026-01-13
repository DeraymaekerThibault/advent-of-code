import sys


def parse_input(content):
    parts = content.strip().split("\n\n")
    ranges = [
        tuple(map(int, line.split("-")))
        for line in parts[0].splitlines()
        if line.strip()
    ]
    ids = (
        [int(line) for line in parts[1].splitlines() if line.strip()]
        if len(parts) > 1
        else []
    )
    return ranges, ids


def merge_ranges(ranges):
    if not ranges:
        return []

    sorted_ranges = sorted(ranges, key=lambda x: x[0])
    merged = [sorted_ranges[0]]

    for current_start, current_end in sorted_ranges[1:]:
        last_start, last_end = merged[-1]

        if current_start <= last_end + 1:
            merged[-1] = (last_start, max(last_end, current_end))
        else:
            merged.append((current_start, current_end))

    return merged


def solve(input_file="2025/05/input.txt"):
    with open(input_file, "r") as f:
        content = f.read()

    ranges, available_ids = parse_input(content)

    # Part 1
    fresh_count = sum(
        1 for iid in available_ids if any(start <= iid <= end for start, end in ranges)
    )
    print(f"Part 1 - Fresh ingredients: {fresh_count}")

    # Part 2
    merged = merge_ranges(ranges)
    total_fresh = sum(end - start + 1 for start, end in merged)
    print(f"Part 2 - Total fresh IDs: {total_fresh}")


if __name__ == "__main__":
    solve(sys.argv[1] if len(sys.argv) > 1 else "2025/05/input.txt")
