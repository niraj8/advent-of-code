import sys

def parse_input():
    user_input = sys.stdin.read()
    energies = []
    current_elf_energy = 0
    for line in user_input.split("\n"):
        if line != "":
            current_elf_energy += int(line)
        else:
            energies.append(current_elf_energy)
            current_elf_energy = 0
    energies.append(current_elf_energy)
    return energies

energies = parse_input()
print(max(energies))

top3 = sorted(energies, reverse=True)[0:3]
print(sum(top3))
