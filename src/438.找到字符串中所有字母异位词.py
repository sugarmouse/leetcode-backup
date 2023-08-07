#
# @lc app=leetcode.cn id=438 lang=python3
#
# [438] 找到字符串中所有字母异位词
#

from typing import List
from collections import defaultdict

# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        left, right = 0, 0
        need, window = defaultdict(int), defaultdict(int)

        valid = 0
        res = []
        for c in p:
            need[c] += 1

        while right < len(s):
            # 移动 right 找复合要求的子字符串
            c = s[right]
            right += 1
            if c in need:
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1

            while right - left >= len(p):
                # 此时子字符串 s1[left, right] 的长度等于 len(s2)
                # [left, right)
                if valid == len(need):
                    res.append(left)

                d = s[left]
                left += 1
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
        return res
# @lc code=end

