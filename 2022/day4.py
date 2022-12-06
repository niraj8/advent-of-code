def parse(buffer):
    def str_range_to_int_range(str_range):
        return [int(x) for x in str_range.split("-")]

    return [
        [str_range_to_int_range(ranges[0]), str_range_to_int_range(ranges[1])]
        for ranges in [line.split(",") for line in buffer.split("\n")]
    ]


def has_full_overlap(pair):
    range1 = pair[0]
    range2 = pair[1]

    # list starting with the smaller number or the larger list should be range1
    if range1[0] == range2[0]:
        if range1[1] < range2[1]:
            range1, range2 = range2, range1
    elif range1[0] > range2[0]:
        range1, range2 = range2, range1

    return range1[1] >= range2[1]

def has_overlap(pair):
    return True

def part1(pairs):
    return len(list(filter(has_full_overlap, pairs)))

def part2(pairs):
    return len(list(filter(has_overlap, pairs)))

with open("day4.in", "r") as reader:
    pairs = parse(reader.read())
    print(part1(pairs))
    print(part2(pairs))
