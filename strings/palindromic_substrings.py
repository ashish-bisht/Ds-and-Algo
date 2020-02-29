def count_substrings(s):

    # printing all the substrings
    substrings = []
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            substrings.append(s[i:j])
    count = 0
    for string in substrings:
        if string == string[::-1]:
            count += 1

    return count


s = 'aaa'

print(count_substrings(s))
