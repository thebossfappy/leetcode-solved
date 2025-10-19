"""
    Question: Power of Four
    Desc:   Given an integer n, return True if it is a power of four. 
            Otherwise, return False.
            An integer n is a power of four if there exists an integer x 
            such that n == 4^x.
    URL: https://leetcode.com/problems/power-of-four/
    Resource: Runtime: 28 ms, Memory Usage: 16.5 MB
"""
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # A number is power of four if:
        # 1. It's greater than 0
        # 2. It's a power of two (n & (n-1)) == 0
        # 3. The only set bit is at an even position
        return n > 0 and (n & (n - 1)) == 0 and (n - 1) % 3 == 0
