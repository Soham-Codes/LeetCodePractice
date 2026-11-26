"""
3. Valid Parentheses
Easy
Problem: Given a string containing only (), {}, and [], determine whether the brackets are valid.
Each opening bracket must be closed by the correct type, and brackets must close in the correct order.

Examples:
s = "()[]{}"
# Expected: True
s = "([)]"
# Expected: False

Function:
def isValid(s):
    pass

Suggested time: 20–25 minutes
"""
def isValid(s):
    stack = []
    pairs = {")": "(", "]": "[", "}": "{"}

    for charac in s:
        if charac in "([{":
            stack.append(charac)
        elif charac in ")]}":
            if len(stack) == 0 or stack[-1] != pairs[charac]:
                return False
            stack.pop()
    return len(stack) == 0

s = "()[]{}"
print(f"Result of valid paren: {isValid(s)}")

# All equivalent return not stack, return len(stack) == 0, OR
# if len(stack) == 0:
#   return True
# else:
#   return False

# Where to use Stack?: A stack is useful whenever you need to process things in Last In, First Out (LIFO) order.
# In other words, the last item added is the first item removed.
# You already understand Python lists, so you can implement a stack using append(), pop(), and [-1].

# How to recognize when a problem might need a stack
# Look for statements such as:
# - "Process the most recent item first."
# - "Undo the last operation."
# - "Match nested structures."
# - "Return to the previous state."
# - "Find the next greater or smaller element."
# These are clues that a stack might be useful, although not every problem with these features requires one.