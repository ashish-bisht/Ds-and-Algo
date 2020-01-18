board = [
    [1, 0, 0, 1],
    [0, 0, 0, 1],
    [0, 0, 0, 1]
]


def battleship(board):
    """
    :type :board List[List]
    :rype int
    """
    count = 0
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == 0:
                continue
            # if this condition meets then we can continue as the above one is also same
            if row > 0 and board[row-1][col]:
                continue
            # if this condition meets then we can continue as the right one is also same
            if col > 0 and board[row][col-1]:
                continue
        count += 1


print(battleship(board))
