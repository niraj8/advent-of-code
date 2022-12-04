import string

def parse(buff):
    return [rucksack for rucksack in buff.split("\n")]


priority = {}

for chr in string.ascii_lowercase:
    priority[chr] = ord(chr) - 96
for chr in string.ascii_uppercase:
    priority[chr] = ord(chr) - 64 + 26


def part1(rucksacks):
    priorities_sum = 0 
    for rucksack in rucksacks:
        compartment1 = set(rucksack[0:int(len(rucksack)/2)])
        compartment2 = set(rucksack[int(len(rucksack)/2):])
        priorities_sum += priority[compartment1.intersection(compartment2).pop()]
    return priorities_sum


def part2(rucksacks):
    priorities_sum = 0
    for i in range(0,int(len(rucksacks)/3)):
        rucksack_group = rucksacks[i*3 : i*3+3]
        sack_set_list = [set(sack) for sack in rucksack_group]
        badge = sack_set_list[0].intersection(sack_set_list[1]).intersection(sack_set_list[2])
        priorities_sum += priority[badge.pop()]
    return priorities_sum


with open("day3.in", "r") as reader:
    rucksacks = parse(reader.read())
    print(part1(rucksacks))
    print(part2(rucksacks))
