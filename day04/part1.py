import argparse
import pytest


def check_bounds(x, y, line, lines):
    if x >= 0 and y >= 0 and x < len(line) and y < len(lines):
        return True

    return False


def check_for_xmas(lines, line, idx_x, idx_y):

    total_xmas_from_starting_point = 0

    cardinal_positions = [
        # right, left, down, up
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1),
        # diagonal
        (1, 1),
        (-1, -1),
        (1, -1),
        (-1, 1),
    ]

    for pos_x, pos_y in cardinal_positions:
        new_idx_x = idx_x + pos_x
        new_idx_y = idx_y + pos_y

        if check_bounds(new_idx_x, new_idx_y, line, lines):

            if lines[new_idx_y][new_idx_x] == "M":

                new_idx_x += pos_x
                new_idx_y += pos_y

                if (
                    check_bounds(new_idx_x, new_idx_y, line, lines)
                    and lines[new_idx_y][new_idx_x] == "A"
                ):
                    new_idx_x += pos_x
                    new_idx_y += pos_y

                    if (
                        check_bounds(new_idx_x, new_idx_y, line, lines)
                        and lines[new_idx_y][new_idx_x] == "S"
                    ):
                        total_xmas_from_starting_point += 1

    return total_xmas_from_starting_point


def compute(data):
    result = 0
    lines = data.splitlines()

    for idx_y, y in enumerate(lines):
        for idx_x, x in enumerate(y):

            # Start of 'XMAS'
            if x == "X":
                result += check_for_xmas(lines, y, idx_x, idx_y)

    return result


INPUT = """\
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""


@pytest.mark.parametrize(("test_input,expected"), [(INPUT, 18)])
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
