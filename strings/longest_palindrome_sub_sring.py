def longest_palindrome(s):
    res = ""
    for i in range(len(s)):
        odd = palindrome_helper(s, i, i)
        even = palindrome_helper(s, i, i+1)
        res = max(odd, even, res, key=len)
    return res


def palindrome_helper(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1

    # as the count again increases and while loop got exausted we used one index + for start and 1 - for end, hence [left+1:right]
    return s[left+1:right]


if __name__ == "__main__":
    s = 'nitin'
    print(longest_palindrome(s))
