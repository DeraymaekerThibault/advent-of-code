import pathlib
import sys
from collections import Counter


def solve(path):
    grid = pathlib.Path(path).read_text(encoding="utf-8").splitlines()
    active_columns = {grid[0].index("S")}
    splits = 0

    for row in grid:
        next_active_columns = set()
        for column in active_columns:
            if row[column] == "^":
                splits += 1
                next_active_columns.add(column + 1)
                next_active_columns.add(column - 1)
            else:
                next_active_columns.add(column)
        active_columns = next_active_columns

    return splits


def solve_part2(path):
    grid = pathlib.Path(path).read_text(encoding="utf-8").splitlines()
    active_columns = Counter({grid[0].index("S"): 1})

    for row in grid:
        next_active_columns = Counter()
        for column, count in active_columns.items():
            if row[column] == "^":
                next_active_columns[column + 1] += count
                next_active_columns[column - 1] += count
            else:
                next_active_columns[column] += count
        active_columns = next_active_columns

    return sum(active_columns.values())


if __name__ == "__main__":
    input_path = sys.argv[1] if len(sys.argv) > 1 else "2025/07/input.txt"
    print(f"Part 1: {solve(input_path)}")
    print(f"Part 2: {solve_part2(input_path)}")
