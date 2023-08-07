#
# @lc app=leetcode.cn id=567 lang=python3
#
#
# [567] 字符串的排列

# @lc code=start
from collections import defaultdict

class Solution1:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left, right = 0, 0
        need, window = defaultdict(int), defaultdict(int)

        valid = 0

        for c in s1:
            need[c] += 1

        while right < len(s2):
            # 移动 right 找复合要求的子字符串
            c = s2[right]
            right += 1
            if c in need:
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1

            while right - left >= len(s1):
                # 此时子字符串 s1[left, right] 的长度等于 len(s2)
                # [left, right)
                if valid == len(need):
                    return True

                d = s2[left]
                left += 1
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
        return False
# @lc code=end
