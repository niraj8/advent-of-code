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


with open("day8.in", "r") as reader:
    tree_heights = parse_input(reader.read())
    visible_trees_count = 4 * len(tree_heights) - 4
    for y in range(1, len(tree_heights) - 1):
        for x in range(1, len(tree_heights) - 1):
            if visible(x, y, tree_heights):
                visible_trees_count += 1
    print(visible_trees_count)
