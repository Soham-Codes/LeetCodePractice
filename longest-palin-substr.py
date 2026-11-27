"""
4. Longest Palindromic Substring
Medium
Problem: Given a string s, return its longest contiguous substring that is a palindrome.

A substring consists of consecutive characters. If multiple longest palindromes exist, returning any one is acceptable.

Examples:
s = "babad"
# Expected: "bab" or "aba"
s = "cbbd"
# Expected: "bb"

Function:
def longestPalindrome(s):
    pass

Suggested time: 25–35 minutes
"""
def longestPalindrome(s):
    all_palins = []
    for i in range(0, len(s)):
        list_string = list(s[i:])
        while len(list_string) != 0:
            rev_string = list_string[::-1]
            if rev_string == list_string:
                new_palin = ''.join(list_string)
                all_palins.append(new_palin)
            list_string.pop()
    max_long = 0
    max_indx = 0
    for indx in range(0, len(all_palins)):
        palin = all_palins[indx]
        if len(palin) > max_long:
            max_long = len(palin)
            max_indx = indx
    return all_palins[max_indx]

s = "babad"
print(f"The longest palindrome substring of {s} is: {longestPalindrome(s)}")