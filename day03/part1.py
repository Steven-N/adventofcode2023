import argparse
import pytest
import re


def compute(data):

    mul_regex = r"mul\(\d+,\d+\)"
    num_regex = r"\d+"

    result = 0
    matches = re.findall(mul_regex, data)

    for match in matches:
        numbers = [int(num) for num in re.findall(num_regex, match)]
        result += numbers[0] * numbers[1]

    return result


INPUT = """
xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
"""


@pytest.mark.parametrize(("test_input,expected"), [(INPUT, 161)])
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
