def parse(buffer):
    lines = [line for line in buffer.split("\n")]
    return lines


def part1(lines):
    for line in lines:
        print(end_index_4_consecutive_uniq_chars(line))


def end_index_4_consecutive_uniq_chars(s):
    i = 0
    while i < len(s) - 3:
        if len(set(s[i : i + 4])) == 4:
            return i + 4
        else:
            i += 1


def part2():
    return True


with open("day6.in", "r") as reader:
    lines = parse(reader.read())
    part1(lines)
    # print(part2(crates, moves))
