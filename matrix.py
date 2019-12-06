# creating two dimensional array in python and getting row, col values if ele is ==0.
def print_if_zero(matrix):

    result = []

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == 0:
                result.append([row, col])

    return result


if __name__ == "__main__":
    matrix = [[1, 0, 0], [1, 1, 0], [0, 0, 1], [0, 0, 1]]

    print(print_if_zero(matrix))
