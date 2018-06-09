
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/#/description

class Solution(object):
    """
    Run time: 78ms
    Time complexity: O(n)
    Sapce complexity: O(1)
    """
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return len(nums)

        count = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                count += 1
                nums[count - 1] = nums[i]
        return count

    print(removeDuplicates(None, [1, 1, 2]))
