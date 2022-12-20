def parse_input(buffer):
    return [[int(s) for s in line] for line in buffer.split("\n")]


def visible_from_left(x_coord, y_coord, tree_heights_matrix):
    tree_height = tree_heights_matrix[x_coord][y_coord]
    for y1 in range(0, y_coord):
        height_of_tree_on_the_left = tree_heights[x_coord][y1]
        if height_of_tree_on_the_left >= tree_height:
            return False
    return True


def visible_from_right(x_coord, y_coord, tree_heights_matrix):
    tree_height = tree_heights_matrix[x_coord][y_coord]
    for y1 in range(y_coord + 1, len(tree_heights_matrix)):
        height_of_tree_on_the_right = tree_heights[x_coord][y1]
        if height_of_tree_on_the_right >= tree_height:
            return False
    return True


def visible_from_top(x_coord, y_coord, tree_heights_matrix):
    tree_height = tree_heights_matrix[x_coord][y_coord]
    for x1 in range(0, x_coord):
        height_of_tree_on_the_top = tree_heights_matrix[x1][y_coord]
        if height_of_tree_on_the_top >= tree_height:
            return False
    return True


def visible_from_bottom(x_coord, y_coord, tree_heights_matrix):
    tree_height = tree_heights_matrix[x_coord][y_coord]
    for x1 in range(x_coord + 1, len(tree_heights_matrix)):
        height_of_tree_on_the_bottom = tree_heights_matrix[x1][y_coord]
        if height_of_tree_on_the_bottom >= tree_height:
            return False
    return True


def visible(x_coord, y_coord, tree_heights_matrix):
    return visible_from_left(x_coord, y_coord, tree_heights_matrix) or \
           visible_from_top(x_coord, y_coord, tree_heights_matrix) or \
           visible_from_right(x_coord, y_coord, tree_heights_matrix) or \
           visible_from_bottom(x_coord, y_coord, tree_heights_matrix)


def part1():
    visible_trees_count = 4 * len(tree_heights) - 4
    for y in range(1, len(tree_heights) - 1):
        for x in range(1, len(tree_heights) - 1):
            if visible(x, y, tree_heights):
                visible_trees_count += 1
    return visible_trees_count


def scenic_score(x_coord, y_coord, tree_heights_matrix, transposed):
    tree_height = tree_heights_matrix[x_coord][y_coord]

    trees_on_left = list(reversed(tree_heights_matrix[x_coord][0:y_coord]))
    trees_on_right = tree_heights_matrix[x_coord][y_coord + 1:]
    trees_on_top = list(reversed(transposed[y_coord][:x_coord]))
    trees_on_bottom = transposed[y_coord][x_coord + 1:]

    visible_left = trees_visible(tree_height, trees_on_left)
    visible_top = trees_visible(tree_height, trees_on_top)
    visible_right = trees_visible(tree_height, trees_on_right)
    visible_bottom = trees_visible(tree_height, trees_on_bottom)

    return visible_left * visible_top * visible_right * visible_bottom


def trees_visible(this_tree_height, heights):
    count = 0
    for height in heights:
        if height < this_tree_height:
            count += 1
        elif height >= this_tree_height:
            count += 1
            break
    return count


def part2(tree_heights_matrix):
    max_score = 0
    transposed = list(map(list, zip(*tree_heights_matrix)))

    for q in range(0, len(tree_heights)):
        for p in range(0, len(tree_heights)):
            tree_score = scenic_score(p, q, tree_heights_matrix, transposed)
            if tree_score > max_score:
                max_score = tree_score
    return max_score


with open("day8.in", "r") as reader:
    tree_heights = parse_input(reader.read())

    print(part1())
    print(part2(tree_heights))
