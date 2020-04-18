def search_2d_matrix(matrix, target):
    if not matrix:
        return False
    number_row = len(matrix)
    number_col = len(matrix[0])

    left = 0
    right = number_row * number_col - 1
    while left <= right:
        mid = (left+right)//2
        num = matrix[mid // number_col][mid % number_col]
        if num == target:
            return True

        elif num > target:
            right = mid-1

        else:
            left = mid + 1
    return False


target = 13
matrix = [
    [1,   3,  5,  7],
    [10, 11, 16, 20],
    [23, 30, 34, 50]
]

print(search_2d_matrix(matrix, target))
