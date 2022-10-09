"""
    Question: Two SUm
    Desc:   Given an array of integers nums and an integer target, 
            return indices of the two numbers such that they add up to target.
            You may assume that each input would have exactly one solution, 
            and you may not use the same element twice.
            You can return the answer in any order.
    URL: https://leetcode.com/problems/two-sum/
    Resource: Runtime: 3393 ms, Memory Usage: 15 MB
"""
class Solution:
    def twoSum(self, nums: int, target: int):
        for idx, x in enumerate(nums):
            for idy, y in enumerate(nums[idx+1:]):
                if y == target-x:
                    return [idx,idy+idx+1]

