def word_search(board, word):
    d = {}

    for row in range(len(board)):
        for col in range(len(board[row])):
            val = board[row][col]
            if val in d.keys():
                d[val] += 1
            else:
                d[val] = 1

    for ch in word:
        if ch in d.keys():
            if d[ch] > 0:
                d[ch] -= 1
            else:
                return False
    return True


board = [
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
]

word = "ABCB"

print(word_search(board, word))
