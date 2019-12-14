from math import sqrt


def perfect_squares(num):
    squares = [i*i for i in range(int(sqrt(num)+1))]
    ways = [float('inf') for i in range(num+1)]
    ways[0] = 0
    for square in squares:
        for i in range(1, num+1):
            if square <= i:
                ways[i] = min(ways[i], 1+ways[i-square])

    return ways[num]


num = 12
print(perfect_squares(num))
