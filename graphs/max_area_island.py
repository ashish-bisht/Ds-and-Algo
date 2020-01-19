# matrix = [
#     [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
#     [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
#     [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]
# ]

matrix = [
    [1, 1, 0, 0, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 1, 1],
    [0, 0, 0, 1, 1]

]

# matrix = [
#     [0, 0, 0, 0, 0]
# ]


def max_area_island(matrix):
    result = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == 1:
                neighbours = dfs(matrix, row, col)
                result = max(result, neighbours)
    return result


def dfs(matrix, row, col):

    if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[row]) or matrix[row][col] == 0:
        return 0

    matrix[row][col] = 0
    up = dfs(matrix, row-1, col)
    down = dfs(matrix, row+1, col)
    left = dfs(matrix, row, col-1)
    right = dfs(matrix, row, col+1)

    return up+down+left+right+1


print(max_area_island(matrix))
