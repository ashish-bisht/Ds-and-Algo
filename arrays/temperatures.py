T = [73, 74, 75, 71, 69, 72, 76, 73]


def daily_temperature(T):
    res = []
    for i in range(len(T)):
        count = 1
        for j in range(i+1, len(T)):
            if T[i] < T[j]:
                res.append(count)
                break
            elif j == len(T)-1:
                res.append(0)
                break

            else:
                count += 1

    return res + [0]


def daily_temperature2(T):
    res = [0 for x in range(len(T))]
    stack = []

    for i, temperature in enumerate(T):
        while stack and T[stack[-1]] < temperature:
            prev_index = stack.pop()
            res[prev_index] = i - prev_index
        stack.append(i)

    return res


print(daily_temperature(T))
print(daily_temperature2(T))
