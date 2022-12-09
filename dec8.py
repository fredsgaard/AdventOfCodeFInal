import csv


def forest():
    with open('dec8.csv') as csv_file:
        csv_reader = csv.reader(csv_file)
        tree_matrix = []
        for row in csv_reader:
            tree_line = []
            for tree in row[0]:
                tree_line.append(tree)
            tree_matrix.append(tree_line)
    return tree_matrix


def visible(tree, line_of_trees):
    tree_visible = True
    for t in line_of_trees:
        if tree <= t:
            tree_visible = False
            break
    return tree_visible

def scenic_score(tree, left_line, right_line, top_line, bottom_line):
    score = 0
    left_vis = 0
    right_vis = 0
    top_vis = 0
    bottom_vis = 0
    for t in left_line:
        if tree <= t:
            left_vis += 1
            break
        left_vis += 1

    for t in right_line:
        if tree <= t:
            right_vis += 1
            break
        right_vis += 1

    for t in top_line:
        if tree <= t:
            top_vis += 1
            break
        top_vis += 1

    for t in bottom_line:
        if tree <= t:
            bottom_vis += 1
            break
        bottom_vis += 1
    score = left_vis * right_vis * top_vis * bottom_vis
    return score
def dec8_part1():
    left = True
    right = True
    top = True
    bottom = True
    tree_matrix = forest()
    visible_count = 0
    # iterate through rows
    for i in range(0, len(tree_matrix) - 1, 1):
        # iterate through columns
        for j in range(0, len(tree_matrix[0]) - 1, 1):
            tree = tree_matrix[i][j]

            # Left
            left_line_of_trees = tree_matrix[i][0:j]
            left = visible(tree, left_line_of_trees)
            if left:
                visible_count += 1
                continue

            # Right
            right_line_of_trees = tree_matrix[i][j + 1:len(tree_matrix[i])]
            right = visible(tree, right_line_of_trees)
            if right:
                visible_count += 1
                continue

            # Get column
            col = [row[j] for row in tree_matrix]
            # Top
            top_line_of_trees = col[0:i]
            top = visible(tree, top_line_of_trees)
            if top:
                visible_count += 1
                continue

            # Bottom
            bottom_line_of_trees = col[i + 1:len(col)]
            bottom = visible(tree, bottom_line_of_trees)
            if bottom:
                visible_count += 1
                continue

    print('Visible trees in forest: ' + str(visible_count))
    edge_trees = 2 * (len(tree_matrix) - 1) + 2 * (len(tree_matrix[0]) - 1)
    print('Visible trees in forest edge: ' + str(edge_trees))
    print('Visible trees: ' + str(visible_count + edge_trees))

def dec8_part2():
    max_score = [0, 0, 0]
    tree_matrix = forest()
    for i in range(0, len(tree_matrix) - 1, 1):
        # iterate through columns
        for j in range(0, len(tree_matrix[0]) - 1, 1):
            tree = tree_matrix[i][j]
            col = [row[j] for row in tree_matrix]

            left_line_of_trees = tree_matrix[i][0:j]
            left_line_of_trees.reverse()
            right_line_of_trees = tree_matrix[i][j + 1:len(tree_matrix[i])]
            top_line_of_trees = col[0:i]
            top_line_of_trees.reverse()
            bottom_line_of_trees = col[i + 1:len(col)]

            score = scenic_score(tree, left_line_of_trees, right_line_of_trees, top_line_of_trees, bottom_line_of_trees)

            if score > max_score[0]:
                max_score = [score, i, j]

    print('Max scenic score: ' + str(max_score[0]) + ' At row: ' + str(max_score[1]) + ' and column: ' + str(max_score[2]))