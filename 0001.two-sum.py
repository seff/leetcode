#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        tmp = {}
        for index, value in enumerate(nums):
            if target - value in tmp:
                return [tmp[target - value], index]
            else:
                tmp[value] = index


def main():
    nums = [2, 7, 11, 15]
    target = 9
    s = Solution()
    print(s.twoSum(nums, target))


if __name__ == '__main__':
    main()
