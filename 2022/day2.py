import sys

def parse(buff):
    return [[round[0], round[2]] for round in buff.split("\n")]

abc = { "A": "Rock", "B": "Paper", "C": "Scissors"}
xyz_part1 = { "X": "Rock", "Y": "Paper", "Z": "Scissors"}
xyz_outcome = { "X": "Loss", "Y": "Draw", "Z": "Win"}
hand_score = { "Rock": 1, "Paper": 2, "Scissors": 3 }
outcome_score = {"Loss": 0, "Draw": 3, "Win": 6}
part1_total = 0
part2_total = 0

def part1_score(opponent_hand, my_hand):
    score = 0
    score += hand_score[my_hand]
    if opponent_hand == my_hand:
        score += 3
    elif opponent_hand == "Rock":
        if my_hand == "Paper":
            score += 6
    elif opponent_hand == "Scissors":
        if my_hand == "Rock":
            score += 6
    elif opponent_hand == "Paper":
        if my_hand == "Scissors":
            score += 6
    return score

def part2_score(oppenent_hand, outcome):
    def choose_winning_hand(hand):
        if hand == "Rock":
            return "Paper"
        elif hand == "Paper":
            return "Scissors"
        elif hand == "Scissors":
            return "Rock"
        else:
            raise Exception("Invalid hand ", hand)

    def choose_losing_hand(hand):
        if hand == "Rock":
            return "Scissors"
        elif hand == "Paper":
            return "Rock"
        elif hand == "Scissors":
            return "Paper"
        else:
            raise Exception("Invalid hand ", hand)

    score = 0
    if outcome == "Draw":
        score += 3 + hand_score[oppenent_hand]
    elif outcome == "Win":
        score += 6 + hand_score[choose_winning_hand(oppenent_hand)]
    elif outcome == "Loss":
        score += 0 + hand_score[choose_losing_hand(oppenent_hand)]
    return score


with open("day2.in", "r") as reader:
    rounds = parse(reader.read())
    for round in rounds:
        part1_total += part1_score(abc[round[0]], xyz_part1[round[1]])
        part2_total += part2_score(abc[round[0]], xyz_outcome[round[1]])
    print(part1_total)
    print(part2_total)

