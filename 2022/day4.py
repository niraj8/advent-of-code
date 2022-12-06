
def parse(buffer):
    def str_range_to_int_range(str_range):
        return [int(x) for x in str_range.split("-")]

    return [ 
        [ str_range_to_int_range(ranges[0]), str_range_to_int_range(ranges[1]) ] for ranges in [line.split(",") for line in buffer.split("\n")]
    ]

def has_full_overlap(pair):
    return True


with open("day4-example.in", "r") as reader:
    pairs = parse(reader.read())
    print(len(list(filter(has_full_overlap, pairs))))
    