from dataclasses import dataclass


@dataclass
class CommandAndOutput:
    command: str
    output: list


@dataclass
class File:
    name: str
    size: int


@dataclass
class Directory:
    name: str
    dirs: list
    files: list


directory_sizes_dict = {}


def parse_input(buffer):
    lines = [line for line in buffer.split("\n")]
    line_index = 0
    commands_and_outputs = []
    while line_index < len(lines):

        line = lines[line_index]
        if line.startswith("$"):
            command = line[2:]
            output_lines_list = []
            while line_index + 1 < len(lines) and "$" not in lines[line_index + 1]:
                line_index += 1
                output_lines_list.append(lines[line_index])
            commands_and_outputs.append(CommandAndOutput(command, output_lines_list))

        line_index += 1

    return commands_and_outputs


def part1(commands):
    directory_tree = parse_directory_tree(commands)
    directory_size(directory_tree, "/")
    return sum([v for (k, v) in directory_sizes_dict.items() if v <= 1_00_000])


def navigate_to_path(directory_tree, path_dir_list):
    current_directory = directory_tree
    for d in path_dir_list[1:]:
        child_dir_names = [child_dir.name for child_dir in current_directory.dirs]
        if d in child_dir_names:
            current_directory = list(filter(lambda child_dir: child_dir.name == d, current_directory.dirs))[0]
        else:
            raise Exception("path unavailable")
    return current_directory


def parse_directory_tree(commands):
    directory_tree = None
    current_directory = None
    path_dir_list = []  # pwd output as a list /foo/bar -> [/, foo, bar]
    for cmd in commands:
        current_command = cmd.command
        if current_command.startswith("cd"):
            change_directory_path = current_command.split(" ")[1]
            if change_directory_path == "..":
                path_dir_list.pop()
                current_directory = navigate_to_path(directory_tree, path_dir_list)
            elif change_directory_path == "/":
                path_dir_list = ["/"]
                if directory_tree is None:
                    directory_tree = Directory("/", [], [])
                current_directory = directory_tree
            else:
                path_dir_list.append(change_directory_path)
                current_directory = navigate_to_path(directory_tree, path_dir_list)

        if current_command.startswith("ls"):
            empty_dirs, files = ls(cmd)
            current_directory.dirs = empty_dirs
            current_directory.files = files
    return directory_tree


def ls(cmd):
    dirs = [Directory(line.split(" ")[1], [], []) for line in
            filter(lambda line: line.startswith("dir"), cmd.output)]
    files = [File(line.split(" ")[1], int(line.split(" ")[0])) for line in
             filter(lambda line: not line.startswith("dir"), cmd.output)]
    return dirs, files


def directory_size(directory, current_path):
    files_size = sum([file.size for file in directory.files])
    dirs_size = sum([
        directory_size(child_dir, current_path + child_dir.name + "/")
        for child_dir in directory.dirs
    ])
    directory_sizes_dict[current_path] = dirs_size + files_size
    return dirs_size + files_size


def part2(commands):
    return commands


with open("day7.in", "r") as reader:
    parsed_input = parse_input(reader.read())
    print(part1(parsed_input))

    # part2(lines)

assert ls(CommandAndOutput("ls", ["584 i"])) == ([], [File("i", 584)])
assert ls(CommandAndOutput("ls", ["dir e", "584 i"])) == ([Directory("e", [], [])], [File("i", 584)])

assert navigate_to_path(Directory("/", [], []), ["/"]) == Directory("/", [], [])
assert navigate_to_path(Directory("/", [Directory("a", [], [])], []), ["/", "a"]) == Directory("a", [], [])
dir_a_with_child_b = Directory("/", [Directory("a", [Directory("b", [], [])], [])], [])
assert navigate_to_path(dir_a_with_child_b, ["/", "a", "b"]) == Directory("b", [], [])
