# coin change problem:::
# formuala used:: if denom <= amount at that loop,  ways[amount] += ways[amount-denom]


def coin_change(denoms, sum):
    ways = [0 for i in range(sum+1)]
    ways[0] = 1
    for denom in denoms:
        for amount in range(1, sum+1):
            if denom <= sum:
                ways[amount] += ways[amount-denom]

    return ways[sum]


if __name__ == "__main__":

    sum = 10
    denoms = [1, 5, 10, 25]

    print(coin_change(denoms, sum))
