# solution for part 2

from enum import Enum


with open("input.txt") as f:
    data = f.readlines()


class Color(str, Enum):
    GREEN = "green"
    RED = "red"
    BLUE = "blue"


def parse_game(line: str) -> str:
    _, play = line.split(":")
    return play


def parse_number_of_cube(text: str) -> int:
    return int(text.strip().split(" ")[0])


def reinit_cube_counter() -> dict[Color, int]:
    return {Color.GREEN: 0, Color.RED: 0, Color.BLUE: 0}


def solver(data: str) -> int:
    total = 0
    for line in data:
        counter = reinit_cube_counter()
        play = parse_game(line)
        for set_ in play.split(";"):
            for cube in set_.split(","):
                for color in counter:
                    if color not in cube:
                        continue
                    counter[color] = max(parse_number_of_cube(cube),
                                         counter[color])
        total += (counter[Color.GREEN]
                  * counter[Color.RED]
                  * counter[Color.BLUE])
    return total


if __name__ == "__main__":
    print(solver(data))
