def max_sub_array(array):
    """
    :type :array List[int]
    :rtype int
    """
    current_max = array[0]
    max_so_far = array[0]
    for i in range(1, len(array)):
        current_num = array[i]
        current_max = max(current_num, current_max+current_num)
        max_so_far = max(current_max, max_so_far)

    return max_so_far


if __name__ == "__main__":
    array = [3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]

    print(max_sub_array(array))
