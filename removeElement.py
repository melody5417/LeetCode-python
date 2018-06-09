
# https://leetcode.com/problems/remove-element/#/description

class Solution(object):
    """
    Run time: 35ms
    Time complexity: O(n)
    Space complexity: O(1)
    """
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        count = 0;
        length = range(0, len(nums))
        for i in length:
            if val != nums[i]:
                nums[count] = nums[i]
                count += 1
        return count

    """
    Run time: 48ms
    Time complexity: O(n)
    Space complexity: O(1)
    """
    def removeElement2(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        length = len(nums)
        while (i < length):
            if nums[i] == val:
                nums[i] = nums[length - 1]
                length -= 1
            else:
                i += 1
        return length


    print(removeElement2(None, [1, 2, 3, 4, 5], 3))
