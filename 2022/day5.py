from dataclasses import dataclass
import copy


def parse(buffer):
    lines = [line for line in buffer.split("\n")]
    crates = parse_crates(filter(lambda line: "[" in line, lines))
    moves = parse_moves(filter(lambda line: "move" in line, lines))
    return crates, moves


def parse_crates(lines):
    parsed_lines = []
    for line in lines:
        parsed_lines.append([line[i] for i in range(1, len(line), 4)])

    # https://stackoverflow.com/a/6473724
    return [
        list(reversed(list(filter(lambda c: c != " ", l))))
        for l in list(map(list, zip(*parsed_lines)))
    ]


@dataclass
class Move:
    """Class for representing a move"""

    count: int
    from_crate: int
    to_crate: int


def parse_moves(lines):
    moves = []
    for line in lines:
        split_line = line.split(" ")
        moves.append(
            Move(int(split_line[1]), int(split_line[3]) - 1, int(split_line[5]) - 1)
        )
    return moves


def part1(crates, moves):
    crates_copy = copy.deepcopy(crates)
    for move in moves:
        crates_copy[move.to_crate].extend(
            reversed(crates_copy[move.from_crate][-move.count :])
        )
        crates_copy[move.from_crate] = crates_copy[move.from_crate][: -move.count]
    return "".join([crate[-1] for crate in crates_copy if len(crate) > 0])


def part2(crates, moves):
    crates_copy = copy.deepcopy(crates)
    for move in moves:
        crates_copy[move.to_crate].extend(crates_copy[move.from_crate][-move.count :])
        crates_copy[move.from_crate] = crates_copy[move.from_crate][: -move.count]
    return "".join([crate[-1] for crate in crates_copy if len(crate) > 0])


with open("day5.in", "r") as reader:
    crates, moves = parse(reader.read())
    print(part1(crates, moves))
    print(part2(crates, moves))
