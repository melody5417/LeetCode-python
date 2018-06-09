
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/#/description

class Solution(object):

	"""
	Runtime: 48ms
	Time complexity: O(logn)
	Space complexity: O(1)
	"""
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l,r = 0, len(numbers) - 1
        while l < r:
            temp = numbers[l] + numbers[r];
            if temp == target:
                return [l+1, r+1]
            elif temp < target:
                l+=1
            elif temp > target:
                r-=1

	"""
	Runtime: 59ms
	Time complexity: O(n)
	Space complexity: O(n)
	"""
    def twoSum2(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for i, num in enumerate(numbers):
            if target-num in dic:
                return [dic[target-num] + 1, i + 1]
            dic[num] = i

    print(twoSum(None, [1,3,5,6,6,7], 8))