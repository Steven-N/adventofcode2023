import argparse
import pytest


def check(nums, is_increasing):
    for idx, num in enumerate(nums[1:], start=1):

        if is_increasing:
            if not (1 <= (num - nums[idx - 1]) <= 3):
                return False
        else:
            if not (1 <= (nums[idx - 1] - num) <= 3):
                return False
    else:
        return True


def compute(data):

    result = 0

    lines = data.splitlines()

    for line in lines:
        nums = [int(num) for num in line.split()]

        is_increasing = nums[0] < nums[1]

        if check(nums, is_increasing):
            result += 1
            continue

        for idx in range(0, len(nums)):
            new_nums = nums[:idx] + nums[idx + 1 :]
            is_increasing = new_nums[0] < new_nums[1]
            if check(new_nums, is_increasing):
                result += 1
                break

    return result


INPUT = """\
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""


@pytest.mark.parametrize(("test_input,expected"), [(INPUT, 4)])
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
