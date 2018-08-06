# coding: utf-8
# 最长的不含重复字母的子字符串


def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    max_length = 0
    start = 0
    char_seen = {}
    for ind, val in enumerate(s):
        if val not in char_seen or char_seen[val] < start:
            max_length = max(max_length, ind - start + 1)
        else:
            start = char_seen[val] + 1
        char_seen[val] = ind
    return max_length
