def fibo_recu(n):
    # very bad as it's time complexity will be exponential as wel as space complexity...
    if n == 1:
        return 1
    if n == 0:
        return 0
    return fibo_recu(n-1) + fibo_recu(n-2)


def fibo_dynamic(n):
    # in dp storing previous things and use them to solve next things, time and space both O(n).
    fib = [0 for i in range(n+1)]
    fib[1] = 1
    for i in range(2, n+1):
        fib[i] = fib[i-1] + fib[i-2]
    return fib[n]


def fibo_tuple(n):
    # time complexity O(n) and space complexity O(1).
    a, b = 0, 1
    if n == 1:
        return a
    if n == 2:
        return b
    for i in range(2, n+1):
        b, a = a+b, b
    return b


def fibo_tail_recursion(n, b=1, a=0):
    # Space and time complexity O(n)
    if n == 0:
        return 0

    if n == 1:
        return b
    return fibo_tail_recursion(n-1, a+b, b)


if __name__ == "__main__":
    print(fibo_recu(9))

    print(fibo_dynamic(9))

    print(fibo_tuple(9))

    print(fibo_tail_recursion(9))
