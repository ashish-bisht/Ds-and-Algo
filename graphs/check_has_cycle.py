array = [2, 3, 1, -4, -4, 2]


def has_single_cycle(array):
    """
    :type :array List[int]
    :rtype Boolean
    """
    start_index = 0
    current_index = 0
    visited_numbers = 0

    while visited_numbers < len(array):
        if visited_numbers > 0 and current_index == start_index:
            return False

        visited_numbers += 1
        current_index = get_next_index(current_index)

    return current_index == start_index


def get_next_index(current_index):
    """
    helper function
    :type current_index int
    :rtype int
    """
    jump = array[current_index]
    # if the sum exceeds the len it will give index error hence %
    next_index = (jump + current_index) % len(array)
    # need to check if it is not negative , if it is add len(array)
    return next_index if next_index >= 0 else next_index + len(array)


print(has_single_cycle(array))
