
# https://leetcode.com/problems/two-sum/#/description

class Solution:

    """
    Run time: 1556 ms
    Time complexity: O(n2)
    Space complexity: O(1)
    """
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        k = 0
        for i in nums:
            k += 1
            if (target - i) in nums[k:]:
                return [nums.index(i), nums[k:].index(target - i) + k]
        return None

    """
    Run time: 56 ms
    Time complexity: O(n)
    Space complexity: O(n)
    """
    def twoSum2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for i, num in enumerate(nums):
            if target - num  in dic:
                return [dic[target - num], i]
            dic[num] = i
        return None


    print(twoSum2(None, (1, 5, 3), 4))