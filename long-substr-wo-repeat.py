"""
5. Longest Substring Without Repeating Characters
Medium
Problem: Given a string s, find the length of the longest contiguous substring that contains no repeated characters.

You only need to return the length, not the substring itself.

Examples:
s = "abcabcbb"
# Expected: 3
s = "bbbbb"
# Expected: 1
s = "pwwkew"
# Expected: 3

Function:
def lengthOfLongestSubstring(s):
    pass

Suggested time: 25–35 minutes
"""
def lengthOfLongestSubstring(s):
    max_streak = 0
    queue = []
    for i in range (0, len(s)):
        char = s[i]
        while char in queue:
            queue.pop(0)
        queue.append(char)
        current_streak = len(queue)
        max_streak = max(max_streak, current_streak)
    return max_streak

s = "abcabcbb"
print(f"The longest substring without repeating character in {s} is: {lengthOfLongestSubstring(s)}")