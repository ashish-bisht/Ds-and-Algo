def tripple_sum(array, sum):
    """
    :type :array List[int]
    :type :sum Int
    :rtype List[List[int]]
    """
    # first sorting them
    array.sort()
    result = []
    for i in range(len(array)-2):
        current_num = array[i]
        left = i+1
        right = len(array)-1

        while left < right:
            current_sum = current_num + array[left] + array[right]

            if current_sum == sum:
                result.append([current_num, array[left], array[right]])
                left += 1
                right -= 1
            if current_sum < sum:
                left += 1
            if current_sum > sum:
                right -= 1
    return result


array = [12, 3, 1, 2, -6, 5, -8, 6]
sum = 0

print(tripple_sum(array, sum))
