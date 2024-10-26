"""
    Question: Merge Sorted Array
    Desc:   
        You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
        Merge nums1 and nums2 into a single array sorted in non-decreasing order.
        The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
    URL: https://leetcode.com/problems/merge-sorted-array/description/
    Resource: Runtime: 3393 ms, Memory Usage: 15 MB
"""

from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Initialize two pointers for the end of valid elements in nums1 and nums2
        p1, p2 = m - 1, n - 1
        # Start filling nums1 from the end
        p = m + n - 1

        # While there are elements to compare in both nums1 and nums2
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

        # If there are remaining elements in nums2, copy them
        # No need to copy nums1 since it's already in place
        nums1[: p2 + 1] = nums2[: p2 + 1]
