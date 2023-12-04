# solution for part 2

from collections import defaultdict
from contextlib import suppress

with open("input.txt") as f:
    data = f.readlines()


def build_set(line: str) -> set[str]:
    return set(val for val in line.split(" ") if val != "")


def parse_line(line: str) -> tuple[set[str], set[str]]:
    line = line.replace("\n", " ")
    winning, game = line.split(":")[1].split("|")
    return build_set(winning), build_set(game)


def solver(data: list[str]) -> int:
    scratchcards = defaultdict(int)
    for index, line in enumerate(data):
        scratchcards[index] += 1
        winning, game = parse_line(line)
        counter = 0
        for number in game:
            if number in winning:
                counter += 1
        with suppress(KeyError):
            for inc in range(counter):
                scratchcards[index + inc + 1] += 1 * scratchcards[index]
    return sum(scratchcards.values())


if __name__ == "__main__":
    print(solver(data))
