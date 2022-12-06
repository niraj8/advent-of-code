def parse(buffer):
    def str_range_to_int_range(str_range):
        int_list = [int(x) for x in str_range.split("-")]
        return range(int_list[0], int_list[1])

    return [
        [str_range_to_int_range(ranges[0]), str_range_to_int_range(ranges[1])]
        for ranges in [line.split(",") for line in buffer.split("\n")]
    ]


def reorder_range_list(range1, range2):
    # list starting with the smaller number or the larger list should be range1
    if range1.start == range2.start:
        if range1.stop < range2.stop:
            range1, range2 = range2, range1
    elif range1.start > range2.start:
        range1, range2 = range2, range1
    return range1, range2


def has_full_overlap(pair):
    range1, range2 = reorder_range_list(pair[0], pair[1])
    return range1.stop >= range2.stop


def has_overlap(pair):
    range1, range2 = reorder_range_list(pair[0], pair[1])
    return range2.start <= range1.stop or range1.stop > range2.stop


def part1(pairs):
    return len(list(filter(has_full_overlap, pairs)))


def part2(pairs):
    return len(list(filter(has_overlap, pairs)))


with open("day4.in", "r") as reader:
    pairs = parse(reader.read())
    print(part1(pairs))
    print(part2(pairs))
