import argparse
import pytest


def compute(data):
    pass


INPUT = """
"""


@pytest.mark.parametrize(("test_input,expected"), [(INPUT, None)])
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
