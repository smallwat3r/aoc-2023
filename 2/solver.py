# solution for part 2

import operator
from functools import reduce
from typing import TypedDict, ValuesView


with open("input.txt") as f:
    data = f.readlines()


def parse_game(line: str) -> str:
    _, play = line.split(":")
    return play


def parse_number_of_cube(text: str) -> int:
    return int(text.strip().split(" ")[0])


class CubeCounter(TypedDict):
    red: int
    green: int
    blue: int


def product(vals: ValuesView) -> int:
    return reduce(operator.mul, vals, 1)


def solver(data: list[str]) -> int:
    total = 0
    for line in data:
        counter = CubeCounter(red=0, green=0, blue=0)
        play = parse_game(line)
        for set_ in play.split(";"):
            for cube in set_.split(","):
                for color in counter:
                    if color not in cube:
                        continue
                    counter[color] = max(parse_number_of_cube(cube),
                                         counter[color])
        total += product(counter.values())
    return total


if __name__ == "__main__":
    print(solver(data))
