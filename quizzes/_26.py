"""
    Question: Remove Duplicates from Sorted Array
    Desc: 
        Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.
        Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.
        Return k after placing the final result in the first k slots of nums.
        Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.
    URL: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
"""

from typing import Optional, List


class Solution:
    def remove_duplicated_from_sorted_array(self, nums: List[int]) -> Optional[int]:
        def replace_duplicated_with_underline(nums: List[int], index: int) -> None:
            for i in range(index, len(nums)):
                nums[i] = "_"

        if not nums:
            return 0
        k = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[k]:
                k += 1
                nums[k] = nums[i]
        replace_duplicated_with_underline(nums, k + 1)
        return k + 1, nums
