# def permute(nums):
#     """
#     :type nums: List[int]
#     :rtype: List[List[int]]
#     """
#     # here we need a global wise list, each time we just append to the result
#     rslt = []
#     count = 0

#     def dfs(temp, elements, count):
#         count += 1
#         print(f'count is {count}')
#         # gather rslt
#         if len(elements) == 0:
#             rslt.append(temp[:])  # still remember to use temp[:]
#         for e in elements:
#             temp.append(e)
#             # backtrack
#             next_elements = elements[:]
#             next_elements.remove(e)
#             dfs(temp, next_elements, count)
#             temp.pop()

#     dfs([], nums, count)  # first is the current result
#     print(rslt)
#     return rslt


# nums = [1, 2, 3]

# print(permute(nums))


def get_permutation(array):
    permutations = []
    permutations_helper(array, [], permutations)
    return permutations


def permutations_helper(array, current_permutation, permutations):
    # no need to append empty permuation i.e ([])
    if not len(array) and len(current_permutation):
        permutations.append(current_permutation)

    else:
        for i in range(len(array)):
            new_array = array[:i] + array[i+1:]
            new_permutation = current_permutation + [array[i]]
            permutations_helper(new_array, new_permutation, permutations)


array = [1, 2, 3]
print(get_permutation(array))
