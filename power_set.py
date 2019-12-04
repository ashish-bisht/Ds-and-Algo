def powerset(array):
    """
    :type :array List[int]
    :rtype List[List[int]]
    """
    subsets = [[]]  # created  subsets , intial will be [] and 2^n.
    for ele in array:
        for i in range(len(subsets)):
            # now for every ele we will add current subset
            current_subset = subsets[i]
            subsets.append(current_subset+[ele])

    return subsets


array = [1, 2, 3]

print(powerset(array))
