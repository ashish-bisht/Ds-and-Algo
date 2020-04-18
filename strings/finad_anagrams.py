def find_anagrams(s, p):
    res = []
    dict = {}
    for ch in s:
        if ch in dict.keys():
            dict[ch] += 1
        else:
            dict[ch] = 1

    for i in range(len(s)):
        if s[i] in dict.keys():
            temp = s[i]
            for j in range(i+1, i+len(p)):
                if s[j] not in dict.keys():
                    break
                else:
                    temp += s[j]
            if len(temp) == len(p):
                res.append(temp)

    print(res)


s = "cbaebabacd"
p = "abc"

print(find_anagrams(s, p))
