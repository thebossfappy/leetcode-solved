"""
    Question: Plus One
    Desc: 
        You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

        Increment the large integer by one and return the resulting array of digits.
    URL: https://leetcode.com/problems/plus-one/description/
    Resource: Runtime: 0ms
"""

from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Start from the end of the array
        for i in range(len(digits) - 1, -1, -1):
            # If the current digit is less than 9, simply increment it and return
            if digits[i] < 9:
                digits[i] += 1
                return digits
            # If the digit is 9, it becomes 0 and we carry over
            digits[i] = 0

        # If we exit the loop, it means all digits were 9, so we add a leading 1
        return [1] + digits
