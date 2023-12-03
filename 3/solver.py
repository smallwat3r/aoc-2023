# solution for part 2

from enum import Enum, IntEnum, auto


with open("input.txt") as f:
    data = f.readlines()


def is_gear(char: str) -> bool:
    return char == "*"


def end_or_start(dir: int, index: int, end: int) -> bool:
    return (dir == -1 and index == 0) or (dir == 1 and index == end)


class Position(Enum):
    ABOVE = auto()
    CURRENT = auto()
    BELOW = auto()


class Direction(IntEnum):
    LEFT = -1
    CURRENT = 0
    RIGHT = 1


# this is very ugly, but hey, it works!
def search(data: list[str], index_data: int,
           line: str, index_line: int,
           pair: list[str], position: Position) -> list[str]:

    operators = {
        Position.ABOVE: 1,
        Position.CURRENT: 0,
        Position.BELOW: -1
    }
    operator = operators[position]

    directions = (Direction.LEFT, Direction.CURRENT, Direction.RIGHT)
    if position == Position.CURRENT:
        directions = (Direction.LEFT, Direction.RIGHT)

    number = []
    skip = False

    for direction in directions:
        construct_number = []
        if skip or end_or_start(direction, index_line, len(line)):
            continue
        char = data[index_data + operator][index_line + direction]
        if char.isdigit():
            if direction == Direction.CURRENT:
                construct_number.extend(number)
                number = []  # reinit
            # won't be more than the length of the line itself, and
            # we will probably break before then
            for i in range(len(line)):
                if direction == Direction.LEFT:
                    i = -i
                char = data[index_data + operator][index_line + direction + i]
                if char.isdigit():
                    if direction < Direction.CURRENT:
                        construct_number.insert(0, char)
                    else:
                        construct_number.append(char)
                else:
                    if i > 0:
                        skip = True
                    break
            number.append("".join(construct_number))
    if number:
        if len(number) > 1:
            pair += [int(n) for n in number]
        else:
            pair.append(int("".join(number)))
    return pair


def solver(data: list[str]) -> int:
    total = 0
    for data_index, line in enumerate(data):
        for line_index, char in enumerate(line):
            if not is_gear(char):
                continue
            pair = []
            # above
            if data_index > 0:
                pair = search(data, data_index,
                              line, line_index,
                              pair, Position.ABOVE)
            # current
            pair = search(data, data_index,
                          line, line_index,
                          pair, Position.CURRENT)
            # below
            if data_index < len(data) - 1:
                pair = search(data, data_index,
                              line, line_index,
                              pair, Position.BELOW)
            assert len(pair) <= 2
            if len(pair) == 2:
                total += pair[0] * pair[1]
    return total


if __name__ == "__main__":
    print(solver(data))
