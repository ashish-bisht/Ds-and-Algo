def validMountainArray(A):
    if len(A) < 3:
        return False
    up = False
    down = False

    for i in range(1, len(A)):
        if A[i-1] == A[i]:
            return False

        if A[i] > A[i-1]:
            up = True

            if down:
                return False

        else:
            down = True

    return up and down


A = [0, 3, 2, 1]
if __name__ == "__main__":
    print(validMountainArray(A))
