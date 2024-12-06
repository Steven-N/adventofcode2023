import argparse
import pytest


def check_bounds(x, y, visited, line, lines):
    new_pos = (x, y)
    if (
        x >= 0
        and y >= 0
        and x < len(line)
        and y < len(lines)
        and new_pos not in visited
    ):
        return True

    return False


def check_for_xmas(lines, line, idx_x, idx_y):

    total_x_mas_from_starting_point = 0

    cardinal_positions = [
        # diagonal
        (1, 1),
        (-1, -1),
        (1, -1),
        (-1, 1),
    ]

    visited = set()

    for pos_x, pos_y in cardinal_positions:
        new_idx_x = idx_x + pos_x
        new_idx_y = idx_y + pos_y

        if check_bounds(new_idx_x, new_idx_y, visited, line, lines):

            if lines[new_idx_y][new_idx_x] == "M":
                new_pos = (new_idx_x, new_idx_y)
                visited.add(new_pos)

                new_idx_x = idx_x - pos_x
                new_idx_y = idx_y - pos_y

                if (
                    check_bounds(new_idx_x, new_idx_y, visited, line, lines)
                    and lines[new_idx_y][new_idx_x] == "S"
                ):
                    new_pos = (new_idx_x, new_idx_y)
                    visited.add(new_pos)
                    total_x_mas_from_starting_point += 1

            elif lines[new_idx_y][new_idx_x] == "S":

                new_pos = (new_idx_x, new_idx_y)
                visited.add(new_pos)

                new_idx_x = idx_x - pos_x
                new_idx_y = idx_y - pos_y

                if (
                    check_bounds(new_idx_x, new_idx_y, visited, line, lines)
                    and lines[new_idx_y][new_idx_x] == "M"
                ):
                    new_pos = (new_idx_x, new_idx_y)
                    visited.add(new_pos)
                    total_x_mas_from_starting_point += 1

    # We need a full "X" so we expect 2 'MAS'
    return total_x_mas_from_starting_point == 2


def compute(data):
    result = 0
    lines = data.splitlines()

    for idx_y, y in enumerate(lines):
        for idx_x, x in enumerate(y):

            # Start of 'X-MAS'
            if x == "A":
                result += check_for_xmas(lines, y, idx_x, idx_y)

    return result


INPUT = """\
.M.S......
..A..MSMS.
.M.S.MAA..
..A.ASMSM.
.M.S.M....
..........
S.S.S.S.S.
.A.A.A.A..
M.M.M.M.M.
..........
"""

# INPUT = """\
# M.S
# .A.
# M.S
# """


@pytest.mark.parametrize(("test_input,expected"), [(INPUT, 9)])
def test(test_input, expected):
    assert compute(test_input) == expected


def main():
    compute(INPUT)
    parser = argparse.ArgumentParser()
    parser.add_argument("file")
    args = parser.parse_args()

    with open(args.file, "r") as f:
        print(compute(f.read()))


if __name__ == "__main__":
    exit(main())
