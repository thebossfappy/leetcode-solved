"""
    Question: Largest Perimeter Triangle
    Desc: Given an integer array nums, return the largest perimeter of a triangle with a non-zero area, formed from three of these lengths. 
          If it is impossible to form any triangle of a non-zero area, return 0.
    URL: https://leetcode.com/problems/largest-perimeter-triangle/
    Resource: Runtime: 226 ms Memory Usage: 15.5 MB
"""

class Solution:
    def largestPerimeter(self, nums:list):
        maxP = 0
        nums.sort()
        for i in range(0,len(nums)-2):
            a,b,c = nums[i],nums[i+1],nums[i+2]
            if a+b>c:
                #semi-perimeter > all sides
                maxP = a+b+c
        return maxP