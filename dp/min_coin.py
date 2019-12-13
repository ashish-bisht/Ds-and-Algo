def min_coin(denoms, amount):
    ways = [float("inf") for i in range(amount+1)]
    ways[0] = 0

    for denom in denoms:
        for current_amount in range(1, amount+1):
            if denom <= current_amount:
                ways[current_amount] = min(
                    ways[current_amount], 1+ways[current_amount-denom])

    return ways[amount] if ways[amount] != float("inf") else -1


if __name__ == "__main__":

    amount = 7
    denoms = [1, 5, 10]

    print(min_coin(denoms, amount))
