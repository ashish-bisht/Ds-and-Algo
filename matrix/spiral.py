def spiral(matrix):

    res = []

    row_start, col_start = 0, 0
    row_end, col_end = len(matrix)-1, len(matrix[0])-1

    while row_start <= row_end and col_start <= col_end:

        # move right, col will change and row will be constant
        for col in range(col_start, col_end+1):
            res.append(matrix[row_start][col])

        row_start += 1

        # move down , col will be same and row will change
        for row in range(row_start, row_end+1):
            res.append(matrix[row][col_end])

        col_end -= 1

        if row_start <= row_end:
            # move left , col will be changed and row will be same
            for col in range(col_end, col_start-1, -1):
                res.append(matrix[row_end][col])

            row_end -= 1

        if col_start <= col_end:
            # move up, col will be same and row will be changed
            for row in range(row_end, row_start-1, -1):
                res.append(matrix[row][col_start])
            col_start += 1

    return res

    print(res)


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


print(spiral(matrix))
