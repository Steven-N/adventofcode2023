import argparse
import pytest


def compute(data):

    result = 0

    left_l = []
    right_l = []

    for line in data.splitlines():
        nums = line.split()
        left_l.append(int(nums[0]))
        right_l.append(int(nums[1]))

    left_l = sorted(left_l)
    right_l = sorted(right_l)

    for idx in range(len(left_l)):
        result += abs(left_l[idx] - right_l[idx])

    return result


INPUT = """\
3   4
4   3
2   5
1   3
3   9
3   3
"""


@pytest.mark.parametrize(("test_input,expected"), [(INPUT, 11)])
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
