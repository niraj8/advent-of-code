from copy import copy
from dataclasses import dataclass
from enum import Enum


class Direction(Enum):
    L = 'LEFT'
    R = 'RIGHT'
    U = 'UP'
    D = 'DOWN'


@dataclass
class Step:
    direction: Direction
    count: int


@dataclass
class Position:
    x: int
    y: int

    def move_left(self):
        self.x -= 1

    def move_right(self):
        self.x += 1

    def move_up(self):
        self.y += 1

    def move_down(self):
        self.y -= 1


def parse_input(buffer):
    return [
        Step(Direction[step[0]], int(step[1]))
        for step in [
            line.split(" ") for line in buffer.split("\n")
        ]
    ]


def part1(steps):
    visited = []
    starting_position = Position(0, 0)
    head_current_position = copy(starting_position)
    tail_current_position = copy(starting_position)
    visited.append(starting_position)
    for step in steps:
        for i in range(step.count):
            # print(step, i)
            if step.direction == Direction.L:
                head_current_position.move_left()
            if step.direction == Direction.R:
                head_current_position.move_right()
            if step.direction == Direction.U:
                head_current_position.move_up()
            if step.direction == Direction.D:
                head_current_position.move_down()
            tail_current_position = next_tail_move(head_current_position, tail_current_position)
            if tail_current_position not in visited:
                visited.append(copy(tail_current_position))
    # print(head_current_position)
    # print(tail_current_position)
    # print(visited)
    return len(visited)


def next_tail_move(head_position: Position, tail_position: Position):
    x_diff = head_position.x - tail_position.x
    y_diff = head_position.y - tail_position.y

    if is_touching(head_position, tail_position):
        return tail_position

    if x_diff > 0:
        tail_position.move_right()
    elif x_diff < 0:
        tail_position.move_left()

    if y_diff > 0:
        tail_position.move_up()
    elif y_diff < 0:
        tail_position.move_down()
    return tail_position


def is_touching(head_position, tail_position):
    x_diff = head_position.x - tail_position.x
    y_diff = head_position.y - tail_position.y
    if head_position == tail_position or \
            (abs(x_diff) == 1 and abs(y_diff) == 1) or \
            (abs(x_diff) == 1 and abs(y_diff) == 0) or \
            (abs(x_diff) == 0 and abs(y_diff) == 1):
        return True
    else:
        return False


assert is_touching(Position(0, 0), Position(0, 0)) is True
assert is_touching(Position(0, 0), Position(1, 0)) is True
assert is_touching(Position(0, 0), Position(0, 1)) is True
assert is_touching(Position(0, 0), Position(1, 1)) is True

assert is_touching(Position(0, 0), Position(1, 2)) is False
assert is_touching(Position(0, 0), Position(0, 2)) is False
assert is_touching(Position(0, 0), Position(2, 2)) is False

with open("day9.in", "r") as reader:
    steps_list = parse_input(reader.read())
    print(part1(steps_list))
