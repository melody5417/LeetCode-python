# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def isPalindrome1(x):
        """
        :type x: int
        :rtype: bool
        """
        if (x < 0):
            return False        
        reverseX = 0
        absX = abs(x)
        while (absX != 0):
            reverseX = reverseX * 10 + absX % 10
            absX = int(absX / 10)    
        if x == reverseX:
            return True
        return False
    print(isPalindrome1(121))
    
    def isPalindrome2(x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        reverseX, absX = 0, abs(x)
        while absX:
            reverseX = reverseX * 10 + absX % 10
            absX /= 10
        return reverseX == x
    print(isPalindrome2(-121))