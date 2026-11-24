"""
1. Two Sum
Easy
Problem: Given an array of integers nums and an integer target, return the indices of two distinct elements that add up to target.

You may assume exactly one valid answer exists.

Example:
nums = [2, 7, 11, 15]
target = 9
# Expected: [0, 1]

Function:
def twoSum(nums, target):
    pass

Suggested time: 15–20 minutes
"""
def twoSum(nums, target):
    result = []
    for i in range(0, len(nums)):
        for j in range(i+1, len(nums)):
            fixed_num = nums[i]
            var_num = nums[j]
            if (fixed_num + var_num == target):
                result.append(i)
                result.append(j)
    return result

nums = [2, 7, 11, 15]
target = 9
print(f"The result of two-sum is: {twoSum(nums, target)}")