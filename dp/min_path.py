def min_path(matrix):
    paths = [[0 for ele in row] for row in matrix]
    print(paths)

    # paths[0][0] = matrix[0][0]
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if row == 0 and col == 0:
                paths[0][0] = matrix[0][0]

            elif row == 0:
                paths[row][col] = matrix[row][col] + paths[row][col-1]

            elif col == 0:
                paths[row][col] = matrix[row][col] + paths[row-1][col]

            else:
                paths[row][col] = matrix[row][col] + \
                    min(paths[row-1][col], paths[row][col-1])

    print(paths)

    return paths[-1][-1]


if __name__ == "__main__":
    matrix = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]
    print(min_path(matrix))
