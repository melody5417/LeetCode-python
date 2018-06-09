
# https://leetcode.com/problems/search-insert-position/#/description

class Solution(object):

    """
    Run time: 32ms
    Time complexity: O(logn)
    Space Complexity:
    """
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = int((left + right) / 2)
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
        return left

    print(searchInsert(None, [1,2,4,5], 3))
