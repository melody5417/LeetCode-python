# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        absX = abs(x)
        ret = 0
        while(absX != 0):
            ret = ret * 10 + absX % 10
            absX = int(absX / 10)
        if x < 0:
            ret = ret * -1
        if ret < -(2 ** 31) or (ret > 2 ** 31 - 1):
            ret = 0
        return ret