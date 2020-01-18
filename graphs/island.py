def number_islands(matrix):
    count = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == 1:
                dfs(matrix, row, col)
                count += 1

    return count


def dfs(matrix, row, col):
    if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[row]) or matrix[row][col] != 1:
        return
    matrix[row][col] = '#'
    # now will do depth first search to all its neighbours, horizontal and vertical
    dfs(matrix, row-1, col)
    dfs(matrix, row+1, col)
    dfs(matrix, row, col-1)
    dfs(matrix, row, col+1)


matrix = [
    [1, 1, 1, 1, 0],
    [1, 1, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0],
]

print(number_islands(matrix))
