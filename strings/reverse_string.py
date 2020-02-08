def reverse_string(s):
    '''
    total efficeiency will be roughly O(n)
    :type :s string
    :rtype string
    '''
    res = ''
    for char in s:
        res = char + res  # string concatenation in python is  O(n)
    return res


def reverse_string_efficient(s):
    '''
    :type :s string
    :rtype string
    '''
    temp_lst = list(s)
    i, j = 0, len(temp_lst)-1
    while i < j:
        temp_lst[i], temp_lst[j] = temp_lst[j], temp_lst[i]
        i += 1
        j -= 1

    return ''.join(temp_lst)


def reverse_string_recursive(s):
    if len(s) == 0:
        return s

    else:
        return reverse_string_recursive(s[1:]) + s[0]


s = 'ashish'
print(reverse_string(s))
print(reverse_string_efficient(s))
print(reverse_string_recursive(s))
