# remember whenever using recursion write down the base cases first.
# example fibo ::: 0,1,1,2,3,5,8,12....


def recursive_fibo(n):
    """
    :type :n int
    :rtype int
    """
    # here n(2) == 1 and n(1) == 0
    # base case
    if n == 2:
        return 1
    elif n == 1:
        return 0
    else:
        # main logic
        return recursive_fibo(n-1) + recursive_fibo(n-2)


print(recursive_fibo(5))
