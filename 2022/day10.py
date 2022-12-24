class Signal:
    cycles: int


class NOOP(Signal):
    cycles = 1

    def __init__(self) -> None:
        super().__init__()

    def __repr__(self) -> str:
        return "NOOP"

    def run(self, reg):
        return reg


class ADDX(Signal):
    x: int
    cycles = 2

    def __init__(self, x: int) -> None:
        super().__init__()
        self.x = x

    def __repr__(self) -> str:
        return "ADDX<{0}>".format(str(self.x))

    def run(self, reg: int):
        return reg + self.x


def parse_input(buffer):
    def parse_signal(signal_input):
        if "addx" in signal_input:
            signal_arr = signal_input.split(" ")
            return ADDX(int(signal_arr[1]))
        else:
            return NOOP()

    return [parse_signal(line) for line in buffer.split("\n")]


def generate_initial_screen():
    pixel_rows = []
    for row in range(6):
        pixel_row = []
        for pixel in range(40):
            pixel_row.append('.')
        pixel_rows.append(pixel_row)
    return pixel_rows


with open("day10.in", "r") as reader:
    signals = parse_input(reader.read())
    register = 1
    cycles = 0
    signal_strength_sum = 0
    screen = generate_initial_screen()

    for signal in signals:
        for cycle in range(1, signal.cycles + 1):
            cycles += 1
            # print(cycles, signal, register)
            row_index = int((cycles - 1) / 40)
            pixel_index = (cycles - 1) % 40

            if pixel_index == register or register - 1 == pixel_index or register + 1 == pixel_index:
                screen[row_index][pixel_index] = '#'
            signal_strength = cycles * register
            if cycles % 40 == 20:
                signal_strength_sum += signal_strength
            if cycle == signal.cycles:
                register = signal.run(register)

    print(signal_strength_sum)
    for line in screen:
        print(''.join(line))
