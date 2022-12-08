#! /usr/bin/env python3
def load_tree_grid_row_major(file):
    with open(file, 'r') as f:
        return [[tree for tree in row.strip()] for row in f.readlines()]


def transpose(grid):
    return_grid = [[] for _ in range(len(grid[0]))]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            return_grid[j].append(grid[i][j])
    return return_grid


def part1():
    row_major_forest = load_tree_grid_row_major('data')
    row_count = len(row_major_forest)
    col_count = len(row_major_forest[0])
    visible = (row_count * 2) + (col_count * 2) - 4
    col_major_forest = transpose(row_major_forest)

    for i in range(1, row_count-1):
        for j in range(1, col_count-1):
            visible_left = True
            visible_right = True
            visible_top = True
            visible_bottom = True
            for tree in range(0, j):
                if row_major_forest[i][j] <= row_major_forest[i][tree]:
                    visible_left = False
                    break
            for tree in range(j+1, col_count):
                if row_major_forest[i][j] <= row_major_forest[i][tree]:
                    visible_right = False
                    break
            for tree in range(0, i):
                if col_major_forest[j][i] <= col_major_forest[j][tree]:
                    visible_top = False
                    break
            for tree in range(i+1, row_count):
                if col_major_forest[j][i] <= col_major_forest[j][tree]:
                    visible_bottom = False
                    break
            if visible_bottom or visible_top or visible_right or visible_left:
                visible += 1
    print(visible)


def part2():
    row_major_forest = load_tree_grid_row_major('data')
    col_major_forest = transpose(row_major_forest)
    row_count = len(row_major_forest)
    col_count = len(row_major_forest[0])

    highest_scenic_score = 0

    for i in range(0, row_count):
        for j in range(0, col_count):
            tree_scenic_score_left = 0
            tree_scenic_score_right = 0
            tree_scenic_score_up = 0
            tree_scenic_score_down = 0
            for tree in range(j-1, -1, -1):
                tree_scenic_score_left += 1
                if row_major_forest[i][j] <= row_major_forest[i][tree]:
                    break
            for tree in range(j+1, col_count):
                tree_scenic_score_right += 1
                if row_major_forest[i][j] <= row_major_forest[i][tree]:
                    break
            for tree in range(i-1, -1, -1):
                tree_scenic_score_up += 1
                if col_major_forest[j][i] <= col_major_forest[j][tree]:
                    break
            for tree in range(i+1, row_count):
                tree_scenic_score_down += 1
                if col_major_forest[j][i] <= col_major_forest[j][tree]:
                    break

            if tree_scenic_score_left*tree_scenic_score_right*tree_scenic_score_up*tree_scenic_score_down > highest_scenic_score:
                highest_scenic_score = tree_scenic_score_left * \
                    tree_scenic_score_right*tree_scenic_score_up*tree_scenic_score_down
    print(highest_scenic_score)


# part1()
part2()
