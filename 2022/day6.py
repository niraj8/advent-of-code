def parse(buffer):
    lines = [line for line in buffer.split("\n")]
    return lines


def part1(lines):
    for line in lines:
        print(end_index_n_consecutive_uniq_chars(line, 4))


def end_index_n_consecutive_uniq_chars(s, n):
    i = 0
    while i < len(s) - 3:
        if len(set(s[i : i + n])) == n:
            return i + n
        else:
            i += 1


def part2(lines):
    for line in lines:
        print(end_index_n_consecutive_uniq_chars(line, 14))


with open("day6.in", "r") as reader:
    lines = parse(reader.read())
    part1(lines)
    part2(lines)
