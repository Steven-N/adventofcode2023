import argparse
import pytest


def compute(data):

    result = 0

    left_l = []
    right_counts = {}

    for line in data.splitlines():
        nums = line.split()

        left_num = int(nums[0])
        right_num = int(nums[1])
        left_l.append(left_num)

        if right_num not in right_counts:
            right_counts[right_num] = 1
        else:
            right_counts[right_num] += 1

    for num in left_l:
        right_appearances = right_counts.get(num, 0)
        result += num * right_appearances

    return result


INPUT = """\
3   4
4   3
2   5
1   3
3   9
3   3
"""


@pytest.mark.parametrize(("test_input,expected"), [(INPUT, 31)])
def test(test_input, expected):
    assert compute(test_input) == expected


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file")
    args = parser.parse_args()

    with open(args.file, "r") as f:
        print(compute(f.read()))


if __name__ == "__main__":
    exit(main())
