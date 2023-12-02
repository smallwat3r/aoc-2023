# solution for part 2

import math
from dataclasses import dataclass


with open("input.txt") as f:
    data = f.readlines()


@dataclass
class Match:
    pos: int
    value: str | None = None
    value_literal: str | None = None


numeric_map = (
    ("one", "1"), ("two", "2"), ("three", "3"),
    ("four", "4"), ("five", "5"), ("six", "6"),
    ("seven", "7"), ("eight", "8"), ("nine", "9")
)


# this is probably overly complex!
def replace_in_line(line: str, reverse: bool = False) -> str:
    match = Match(math.inf)
    first_digit_index = math.inf
    for i, ele in enumerate(line):
        if ele.isdigit():
            first_digit_index = i
            break
    for k, v in numeric_map:
        if reverse:
            k = k[::-1]
        i = line.find(k)
        if i != -1 and i < match.pos and i < first_digit_index:
            match = Match(i, v, k)
    if match.value:
        line = line.replace(match.value_literal, match.value, 1)
    return line


def clean_up_line(line: str) -> str:
    line = replace_in_line(line)
    line = replace_in_line(line[::-1], reverse=True)
    line = line[::-1]
    return line


@dataclass
class Pointer:
    left: int
    right: int


@dataclass
class Solution:
    first: str = "0"
    last: str = "0"

    def to_digit(self) -> int:
        return int(f"{self.first}{self.last}")


def solver(data: str) -> int:
    total = 0
    for line in data:
        line = clean_up_line(line)
        pointer = Pointer(0, len(line) - 1)
        while pointer.left <= pointer.right:
            solution = Solution()
            if line[pointer.left].isnumeric():
                solution.first = line[pointer.left]
            else:
                pointer.left += 1
            if line[pointer.right].isnumeric():
                solution.last = line[pointer.right]
            else:
                pointer.right -= 1
            if int(solution.first) and int(solution.last):
                break
        total += solution.to_digit()
    return total


if __name__ == "__main__":
    print(solver(data))
