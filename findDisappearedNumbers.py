
# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/#/description

class Solution(object):
	"""
	Runtime: 229ms
	Time complexity: O(n)
	Space complexity: O(n)
	"""
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        marked = set(nums)
        return [i for i in xrange(1, len(nums) + 1) if i not in marked]

    """
    Runtime: 415ms
    Time complexity: O(2n)
    Space complexity: O(1)
    """
    def findDisappearedNumbers2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in xrange(len(nums)):
        index = abs(nums[i]) - 1
        nums[index] = - abs(nums[index])
        return [i + 1 for i in range(len(nums)) if nums[i] > 0]
